from datetime import timedelta

SESSION_TTL = timedelta(minutes=30)


def expires_at(login_time):
    return login_time + SESSION_TTL


def ttl_seconds():
    return SESSION_TTL.seconds // 60
