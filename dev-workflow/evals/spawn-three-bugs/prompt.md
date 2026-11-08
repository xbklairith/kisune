Three unrelated bug reports came in for the services under services/. Look into them in parallel and tell me the root cause of each. Don't change any code yet.

1. Billing: a webhook that keeps failing is sent 4 times, but MAX_ATTEMPTS is 5.
2. Search: searching for "Postgres" finds nothing, while "postgres" finds the right documents.
3. Auth: users are logged out about 30 seconds after they sign in, not after 30 minutes.
