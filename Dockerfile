FROM python:3.11-slim

WORKDIR /app

# Install system dependencies required for psycopg2 / bcrypt
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy dependency files first
COPY pyproject.toml poetry.lock* /app/

# Disable Poetry virtualenv
RUN poetry config virtualenvs.create false

# Install only main dependencies (NOT dev)
RUN poetry install --only main --no-root --no-interaction --no-ansi

# Copy the rest of the code
COPY . /app

# Copy entrypoint and make executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]