import os
from enum import Enum
from typing import TypedDict, Optional

REDIS_BACKEND_URL = os.environ.get('REDIS_BACKEND_URL', 'redis://redis:6379/0')
REDIS_BROKER_URL = os.environ.get('REDIS_BROKER_URL', 'redis://redis:6379/0')
API_SVC_URL = os.environ.get('API_SVC_URL', 'http://API-SERVICE:8000')


class EmailStatus(str, Enum):
    SENT = "SENT"
    FAILED = "FAILED"


class TaskResult(TypedDict):
    status: EmailStatus
    failure_reason: Optional[str]
