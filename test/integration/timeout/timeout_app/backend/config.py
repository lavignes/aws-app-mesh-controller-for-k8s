from os import environ as env
import multiprocessing

PORT = int(env.get("PORT", 8080))
DEBUG_MODE = int(env.get("DEBUG_MODE", 0))
XRAY_APP_NAME = env.get('XRAY_APP_NAME', 'feapp')
WHO_AM_I = env.get('WHO_AM_I', 'backend')
TIMEOUT_VALUE = int(env.get("TIMEOUT_VALUE", 45))

# Gunicorn config
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()
