#!/bin/sh
set -e

# Defaults
DB_PORT=${DB_PORT:-5432}
DB_USER=${DB_USER:-sprintuser}

# Derive DB_HOST from environment or DATABASE_URL, fallback to 'db'
if [ -z "${DB_HOST:-}" ]; then
  if [ -n "${DATABASE_URL:-}" ]; then
    DB_HOST=$(python - <<'PY'
import os
from urllib.parse import urlparse
u = os.getenv('DATABASE_URL')
if u:
    host = urlparse(u).hostname or 'db'
    print(host)
else:
    print('db')
PY
)
  else
    DB_HOST=db
  fi
fi

echo "Waiting for Postgres at ${DB_HOST}:${DB_PORT}..."
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" >/dev/null 2>&1; do
  echo "Postgres is unavailable - sleeping"
  sleep 2
done

echo "Postgres is up - running migrations"
alembic upgrade head

echo "Running seed script (if not already seeded)"
python -m app.seed

echo "Starting uvicorn"
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
