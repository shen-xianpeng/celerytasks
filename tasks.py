import time

from celery import Celery

from celery.task import task

celery = Celery('tasks', broker='amqp://xianpeng:xianpeng@127.0.0.1:5672/proto_v1')
celery.config_from_object('celeryconfig')

@celery.task
def add(x, y):
    return x + y
