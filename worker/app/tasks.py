import logging
from typing import Dict, Tuple

from celery import Celery
from constants import API_SVC_URL, EmailStatus
import requests

logger = logging.getLogger(__name__)
app = Celery('tasks', config_source='config')


@app.task
def debug_task(message: str):
    logger.info(message)
    return message


@app.task
def send_notification(notification_uuid: str, message_body: str, user_email: str) -> Tuple[int, Dict]:
    logger.info(f'Processing notification with uuid: {notification_uuid}')

    # TODO: Use an email client to send user emails
    # Notify the api with email status
    response = requests.patch(
        f'{API_SVC_URL}/notifications/{notification_uuid}',
        {'status': EmailStatus.SENT},
        format="json"
    )
    logger.info(response.json())
    return response.status_code, response.json()
