from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main.views import NotificationSummaryView, NotificationListCreateView, NotificationUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notifications/summary/', NotificationSummaryView.as_view(), name='notification-summary'),
    path('notifications/<uuid:uuid>', NotificationUpdateView.as_view(), name='notification-update'),
    path('notifications/', NotificationListCreateView.as_view(), name='notifications'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
