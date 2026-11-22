"""URL configuration.

Every page lives under a language prefix (`/pt-br/`, `/en/`, `/es/`). A request for `/`
is redirected by `LocaleMiddleware` to the language the browser asks for.
"""

from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from portfolio import views
from portfolio.sitemaps import PortfolioSitemap

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"pages": PortfolioSitemap}}, name="sitemap"),
    path("robots.txt", views.robots, name="robots"),
    path("llms.txt", views.llms_txt, name="llms"),
    path("llms-full.txt", views.llms_full_txt, name="llms-full"),
]

if settings.DEBUG:
    # Share-card sources for scripts/og_images.py; never served in production.
    from portfolio import og

    urlpatterns += [path("og/<str:key>/", og.card, name="og-card")]

urlpatterns += i18n_patterns(
    path("", include("portfolio.urls")),
    prefix_default_language=True,
)

handler404 = "portfolio.views.not_found"
