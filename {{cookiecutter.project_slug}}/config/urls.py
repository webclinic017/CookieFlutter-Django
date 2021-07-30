from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
{%- if cookiecutter.use_async == 'y' %}
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
{%- endif %}
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView
{%- if cookiecutter.use_drf == 'y' %}
from rest_framework.authtoken.views import obtain_auth_token
from rest_auth.views import LogoutView
from {{ cookiecutter.project_slug }}.users.api.views import *
{%- endif %}

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    path(
        "about/", TemplateView.as_view(template_name="pages/about.html"), name="about"
    ),
    # Django Admin, use {% raw %}{% url 'admin:index' %}{% endraw %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("{{ cookiecutter.project_slug }}.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
{%- if cookiecutter.use_async == 'y' %}
if settings.DEBUG:
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()
{%- endif %}
{% if cookiecutter.use_drf == 'y' %}
# API URLS
urlpatterns += [
    # API base url
    path("api/", include("config.api_router")),
    # DRF auth token
    path("api/auth-token/", obtain_auth_token),

    path('api/user/', UserDetailsAPIView.as_view(), name='rest_user_details'),
    path('api/login/', LoginUserView.as_view(), name='account_login'),
    path('api/password/change/', PasswordUserChangeView.as_view(), name='rest_password_change'),
    path('api/password/reset/', PasswordResetUserView.as_view(), name='rest_password_reset'),
    path('api/', include('rest_auth.urls')),
    path('api/registration/', RegisterUserView.as_view(), name='account_signup'),
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/account-confirm-email/<str:key>/', VerifyUserEmailView.as_view(), name='account_confirm_email'),
    path('api/password/reset/confirm/<str:uid>/<str:token>/', PasswordResetConfirmUserView.as_view(), name='rest_password_reset_confirm'),
    path('api/logout/', LogoutView.as_view(), name='rest_logout'),


]
{%- endif %}

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
