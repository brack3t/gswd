from django.conf import settings

import redis


def get_redis_connection():
    """
    Returns a redis connection.
    """
    host = getattr(settings, "REDIS_HOST", "127.0.0.1")
    port = getattr(settings, "REDIS_PORT", 6379)
    db = getattr(settings, "REDIS_DB", 0)

    redis_connection = redis.StrictRedis(
        host=host,
        port=port,
        db=db
    )

    return redis_connection
