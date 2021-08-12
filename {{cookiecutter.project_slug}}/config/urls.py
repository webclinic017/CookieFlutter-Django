
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
{%- if cookiecutter.use_async == 'y' %}
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
{%- endif %}
from django.urls import path, re_path
from django.views import defaults as default_views

from django.conf.urls import include, url 
from django.views.generic import RedirectView 
from {{cookiecutter.project_slug}}.users.api.views import VerifyEmailView 

urlpatterns = [
    url(r'^dj-rest-auth/', include('dj_rest_auth.urls')), 
    url(r'^dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), 
    # https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
    # https://github.com/iMerica/dj-rest-auth/blob/master/dj_rest_auth/registration/urls.py
    re_path(
        r'^dj-rest-auth/account-confirm-email/(?P<key>[-:\w]+)/$',
        VerifyEmailView.as_view(), name='account_email_verification_sent'
    ), 
    url(r'^account/', include('allauth.urls')), 
    url(settings.ADMIN_URL, admin.site.urls), 
    url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path("400/",default_views.bad_request,kwargs={"exception": Exception("Bad Request!")},),
        path("403/",default_views.permission_denied,kwargs={"exception": Exception("Permission Denied")},),
        path("404/",default_views.page_not_found,kwargs={"exception": Exception("Page not Found")},),
        path("500/", default_views.server_error),
    ]
    {%- if cookiecutter.use_async == 'y' %}
    # Static file serving when using Gunicorn + Uvicorn for local web socket development
    urlpatterns += staticfiles_urlpatterns()
    {%- endif %}
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar
        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns


