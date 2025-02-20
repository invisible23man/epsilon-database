# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.7.1 \
    POETRY_HOME="/opt/poetry" \
    PATH="$POETRY_HOME/bin:$PATH" \
    PYTHONPATH=/app

# Additional environment variables for Poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

# Install system dependencies
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# ✅ Ensure Poetry is available in PATH
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy only pyproject.toml and poetry.lock first (to leverage Docker layer caching)
COPY pyproject.toml poetry.lock* /app/

# Install dependencies using Poetry (without installing dev dependencies)
RUN poetry install --no-root

# Copy the entire application code
COPY . /app

# Expose PostgreSQL default port (if needed)
EXPOSE 5432

# Wait for the database to be ready, then run Alembic migrations
# CMD ["sh", "-c", "
#     until nc -z -v -w30 $DB_HOST $DB_PORT; do
#       echo 'Waiting for database connection...'
#       sleep 5
#     done;
#     echo 'Database is ready, running Alembic migrations...';
#     poetry run alembic upgrade head;
#     echo 'Migrations applied successfully!';
#     tail -f /dev/null
# "]
