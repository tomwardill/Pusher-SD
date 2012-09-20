from datetime import timedelta
import celeryconfig
from celery.task import task

import pusher
from serverdensity.api import SDApi, SDServiceError

@celery.task
def hello():
	print "hello world"