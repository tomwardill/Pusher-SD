from datetime import timedelta
import celeryconfig
from celery.task import task

import pusher
from serverdensity.api import SDApi, SDServiceError
from local_settings import *

@celery.task
def hello():
    pusher.app_id = PUSHER_APP_ID
    pusher.key = PUSHER_KEY
    pusher.secret = PUSHER_SECRET

    api = SDApi(
        URL,
        USERNAME,
        PASSWORD,
        API_KEY
    )

    try:
        alerts = api.alerts.getLast()
        alerts = alerts['data']['alerts']
        p = pusher.Pusher()
        p['test_channel'].trigger(‘my_event’, {‘alerts’: alerts})
    except SDServiceError, error:
        pass