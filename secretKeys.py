import os

DJANGO_SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", '5!-u6@glo)knz7xh13xpp##c8+a%y&ml1@soim&w2w^xyr8s1b')
REDIS_HOST = os.getenv("REDIS_HOST", '')
REDIS_PORT = os.getenv("REDIS_PORT", '')
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "robosen_project")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "123456")
