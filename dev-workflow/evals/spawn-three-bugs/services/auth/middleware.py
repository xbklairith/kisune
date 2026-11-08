from datetime import timedelta

from .session import ttl_seconds


def is_expired(now, login_time):
    return now - login_time > timedelta(seconds=ttl_seconds())
