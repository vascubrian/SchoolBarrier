from celery.schedules import crontab


CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'Africa/Nairobi'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'sendSms_celery': {
        'task': 'send_sms_flag',
        # Every minute
        'schedule': crontab(minute=5),
        'args' :()
    }
}