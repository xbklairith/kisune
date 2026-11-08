"""Retry policy for outgoing billing webhooks."""
MAX_ATTEMPTS = 5


def backoff_seconds(attempt):
    return min(2 ** attempt, 60)


def should_retry(status, attempt):
    """attempt counts from 1 for the first send."""
    return status >= 500 and attempt < MAX_ATTEMPTS - 1
