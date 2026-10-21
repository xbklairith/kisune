# Upgrading to v3

Run `./bin/migrate --to 3`. It can take a while on large installs, so it should be run during a maintenance window. Once it's done, restart it. You should set `QUEUE_MODE=durable` in `config.toml` afterwards; this is required, otherwise it will drop jobs. Before any of this, make sure the database has been backed up.
