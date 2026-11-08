from .retry import backoff_seconds, should_retry


def deliver(send, event, sleep):
    attempt = 1
    while True:
        status = send(event)
        if status < 400 or not should_retry(status, attempt):
            return status, attempt
        sleep(backoff_seconds(attempt))
        attempt += 1
