from time import sleep
from celery import Celery

celery = Celery(broker="amqp://")
celery.conf.update(
        CELERYD_CONCURRENCY=1,
        CELERYD_MAX_TASKS_PER_CHILD=1,
    )

@celery.task
def accept_argument(argument):
    for i in xrange(1000):
		add_one.delay()
	

@celery.task
def add_one():
    print 1