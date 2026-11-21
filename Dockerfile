# syntax=docker/dockerfile:1
FROM python:3.14-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

# Build the stylesheet (the Tailwind CLI is downloaded here) and collect hashed static files.
# The key below exists only for these two build commands.
RUN DJANGO_SECRET_KEY=build-only python manage.py tailwind build \
    && DJANGO_SECRET_KEY=build-only python manage.py collectstatic --noinput \
    && rm -rf .django_tailwind_cli

RUN useradd --system --no-create-home app
USER app

EXPOSE 8000
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2", "--no-control-socket", "--access-logfile", "-"]
