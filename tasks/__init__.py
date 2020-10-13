form celery import Celery
import config

def make_selery():
	celery = Celery(__name__, broker=config.CELERY_BROKER)
	celery.conf.update(config.as_dict())
	return celery

celery = make_celery()