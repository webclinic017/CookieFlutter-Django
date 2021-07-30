from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
{%- if cookiecutter.use_async == 'y' %}
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
{%- endif %}
from django.urls import include, path
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

    #https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html
    path('api/rest-auth/', include('rest_auth.urls')),
    # /rest-auth/login/ (POST)
    ### POST: username, email, password
    ### Returns: Token Key
    # /rest-auth/logout/ (POST)
    ### NOTE: ACCOUNT_LOGOUT_ON_GET = True to allow logout using GET 
    # /rest-auth/password/reset/ (POST)
    ### POST: email
    # /rest-auth/password/reset/confirm/ (POST)
    ### POST: uid, token, new_password1, new_password2
    ### NOTE: uid and token are sent in email after calling /rest-auth/password/reset/
    # /rest-auth/password/change/ (POST)
    ### POST: new_password1, new_password2, old_password
    ### NOTE: OLD_PASSWORD_FIELD_ENABLED = True to use old_password.
    ### NOTE: LOGOUT_ON_PASSWORD_CHANGE = False to keep the user logged in after password change
    # /rest-auth/user/ (GET, PUT, PATCH)
    ### POST: username, first_name, last_name
    ### Returns: pk, username, email, first_name, last_name

    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    # /rest-auth/registration/ (POST)
    ### POST: username,password1,password2, email
    # /rest-auth/registration/verify-email/ (POST)
    ### POST: key

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
