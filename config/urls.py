"""URL configuration.

Every page lives under a language prefix (`/pt-br/`, `/en/`, `/es/`). A request for `/`
is redirected by `LocaleMiddleware` to the language the browser asks for.
"""

from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import TemplateView

from portfolio.sitemaps import PortfolioSitemap

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"pages": PortfolioSitemap}}, name="sitemap"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]

urlpatterns += i18n_patterns(
    path("", include("portfolio.urls")),
    prefix_default_language=True,
)

handler404 = "portfolio.views.not_found"
