import logging

logging_config = dict(
    version = 1,
    formatters = {
        'f': {'format':
              '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
        },
    handlers = {
        'd': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG},
        },
    root = {
        'handlers': ['d'],
        'level': logging.INFO,
        }
)
