CELERYBEAT_SCHEDULE = {
    'runs-every-30-seconds': {
        'task': 'tasks.hello',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },
}