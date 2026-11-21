"""Settings for the portfolio site.

One module, configured by environment variables (see `.env.example`). The site has no
database: content lives in `portfolio/content/` and is rendered by templates.
"""

from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def load_env_file(path: Path) -> None:
    """Read `KEY=value` lines from `.env` into the environment, without overriding it."""
    if not path.exists():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        os.environ.setdefault(key.strip(), value.strip().strip("'\""))


load_env_file(BASE_DIR / ".env")


def env_bool(name: str, default: bool = False) -> bool:
    return os.environ.get(name, str(default)).strip().lower() in {"1", "true", "yes", "on"}


def env_list(name: str, default: str = "") -> list[str]:
    return [item.strip() for item in os.environ.get(name, default).split(",") if item.strip()]


DEBUG = env_bool("DJANGO_DEBUG", default=False)

# The development key only exists so `runserver` works out of the box with DJANGO_DEBUG=1.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY") or ("dev-only-not-a-secret" if DEBUG else "")
if not SECRET_KEY:
    raise RuntimeError("Set DJANGO_SECRET_KEY (or DJANGO_DEBUG=1 for local development).")

ALLOWED_HOSTS = env_list("DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1,[::1]" if DEBUG else "")
CSRF_TRUSTED_ORIGINS = env_list("DJANGO_CSRF_TRUSTED_ORIGINS")

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django_tailwind_cli",
    "portfolio",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.gzip.GZipMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.template.context_processors.i18n",
                "portfolio.context_processors.site",
            ],
        },
    },
]

DATABASES: dict[str, dict[str, str]] = {}

# --- Languages -------------------------------------------------------------------------
# Copy is written in Portuguese and translated to English and Spanish. `LocaleMiddleware`
# picks the language from the URL prefix, then from the browser's Accept-Language header;
# a browser that asks for none of the three gets English.
LANGUAGE_CODE = "en"
LANGUAGES = [
    ("pt-br", "Português"),
    ("en", "English"),
    ("es", "Español"),
]
USE_I18N = True
USE_TZ = True
TIME_ZONE = "America/Sao_Paulo"

# --- Static files ----------------------------------------------------------------------
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STORAGES = {
    "staticfiles": {
        "BACKEND": (
            "django.contrib.staticfiles.storage.StaticFilesStorage"
            if DEBUG
            else "whitenoise.storage.CompressedManifestStaticFilesStorage"
        ),
    },
}

# Tailwind v4 through the standalone CLI: no Node in the project.
TAILWIND_CLI_VERSION = "4.3.5"
TAILWIND_CLI_SRC_CSS = "theme/app.css"
TAILWIND_CLI_DIST_CSS = "css/app.css"

# --- Security --------------------------------------------------------------------------
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
X_FRAME_OPTIONS = "DENY"
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = env_bool("DJANGO_SECURE_SSL_REDIRECT", default=True)
    SECURE_HSTS_SECONDS = int(os.environ.get("DJANGO_HSTS_SECONDS", "31536000"))
    # The site lives on the company's root domain, next to other services on subdomains: forcing HTTPS
    # on every subdomain for a year is a separate decision, off unless asked for.
    SECURE_HSTS_INCLUDE_SUBDOMAINS = env_bool("DJANGO_HSTS_INCLUDE_SUBDOMAINS", default=False)

# --- Site ------------------------------------------------------------------------------
# Public origin, used for canonical and hreflang URLs.
SITE_URL = os.environ.get("SITE_URL", "http://localhost:8000").rstrip("/")
# Optional public e-mail shown in the contact section. Leave empty to show only the links.
CONTACT_EMAIL = os.environ.get("CONTACT_EMAIL", "")
# Optional link to this site's public repository, shown in the footer.
REPO_URL = os.environ.get("REPO_URL", "")
