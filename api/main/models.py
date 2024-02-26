import uuid
from django.db import models


class NotificationStatus(models.TextChoices):
    PROCESSING = 'PROCESSING', 'Processing'
    SUCCESSFUL = 'SUCCESSFUL', 'Successful'
    FAILED = 'FAILED', 'Failed'


class Notification(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField(help_text='The notification message')
    # creator = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule = models.CharField(
        help_text='Represents a crontab value. If null, the notification will directly be sent once.',
        null=True,
        blank=True,
        max_length=50
    )
    status = models.CharField(max_length=10, choices=NotificationStatus.choices, default=NotificationStatus.PROCESSING)

    class Meta:
        ordering = ['created_at']
