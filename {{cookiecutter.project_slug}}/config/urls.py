from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
{%- if cookiecutter.use_async == 'y' %}
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
{%- endif %}
from django.urls import include, path, re_path
from django.views import defaults as default_views
from django.views.generic import TemplateView, RedirectView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path("", TemplateView.as_view(template_name="base.html"), name="base"),

    path(settings.ADMIN_URL, admin.site.urls),

    # API base url
    path("api/", include("config.api_router")),

    # DRF auth token
    path("api/auth-token/", obtain_auth_token),

    # This is used for user reset password
    path('', include('django.contrib.auth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),

    path("users/", include("{{ cookiecutter.project_slug }}.users.urls", namespace="users")),
    # path("accounts/", include("allauth.urls")),



    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    {%- if cookiecutter.use_async == 'y' %}
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()
    {%- endif %}
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
