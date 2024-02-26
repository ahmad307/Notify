import logging

from django.db.models import Count, Q
from django.utils.timezone import localtime
from rest_framework.response import Response

from main.models import Notification, NotificationStatus
from rest_framework import generics, serializers, status
from api.celery import app as celery_app


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['uuid', 'status', 'schedule', 'created_at', 'body']
        read_only_fields = ['status', 'uuid', 'created_at']


class NotificationSummarySerializer(serializers.Serializer):
    successful = serializers.IntegerField()
    processing = serializers.IntegerField()
    failed = serializers.IntegerField()


class NotificationSummaryView(generics.ListAPIView):
    serializer_class = NotificationSummarySerializer

    def get_queryset(self):
        return Notification.objects.filter().annotate(
            successful=Count("status", filter=Q(status=NotificationStatus.SUCCESSFUL)),
            failed=Count("status", filter=Q(status=NotificationStatus.FAILED)),
            processing=Count("status", filter=Q(status=NotificationStatus.PROCESSING)),
        )


class NotificationListCreateView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        logging.info(request.data)
        serializer.is_valid(raise_exception=True)
        logging.info(serializer.validated_data)
        notification = serializer.save()

        celery_app.send_task("tasks.send_notification", kwargs={
            "notification_uuid": str(notification.uuid),
            'message_body': notification.body,
            # TODO: send user's email after adding authentication
            'user_email': ''
        })

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NotificationUpdateView(generics.GenericAPIView):
    serializer_class = NotificationSerializer
    lookup_url_kwarg = 'uuid'

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)