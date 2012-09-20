from datetime import timedelta
CELERYBEAT_SCHEDULE = {
    'runs-every-30-seconds': {
        'task': 'tasks.hello',
        'schedule': timedelta(seconds=10),
        'args': (16, 16)
    },
}
