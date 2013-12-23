# The application level settings of workjournal web app

PROJECT = 'workjournal'

LOCALE = 'en_US'

PROCESSES = 1

PORT = 8000

DEBUG = True

LOGGING = 'INFO'

LOG_REQUEST = True

LOG_RESPONSE = False

TIME_ZONE = 'Asia/Shanghai'

STATIC_PATH = 'static'

TEMPLATE_PATH = 'templates'

LOGGING_IGNORE_URLS = [
    '/favicon.ico',
]
