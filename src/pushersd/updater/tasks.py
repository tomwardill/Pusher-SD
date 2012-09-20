from datetime import timedelta
import celeryconfig
from celery.task import task

@celery.task
def hello():
	print "hello world"