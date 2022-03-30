from .common import *


DEBUG = True

import os


# # redis-cache
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://{0}:{1}/0".format(REDIS_HOST, REDIS_PORT),
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#
#     }
# }