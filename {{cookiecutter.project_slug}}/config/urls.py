
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
{%- if cookiecutter.use_async == 'y' %}
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
{%- endif %}
from django.urls import path 
from django.views import defaults as default_views
from django.views.generic import TemplateView

from django.conf.urls import include, url # NEWADD
from django.views.generic import RedirectView # NEWADD
from drf_yasg.views import get_schema_view # NEWADD
from drf_yasg import openapi # NEWADD

from dj_rest_auth.registration.views import VerifyEmailView # NEWADD2

schema_view = get_schema_view(openapi.Info(title='API Docs',default_version='v1',)) # NEWRM


urlpatterns = [

    url(r'^$', TemplateView.as_view(template_name="home.html"), name='home'), # NEWADD
    url(r'^signup/$', TemplateView.as_view(template_name="signup.html"), name='signup'), # NEWADD
    url(r'^email-verification/$', TemplateView.as_view(template_name="email_verification.html"), name='email-verification'), # NEWADD
    url(r'^login/$', TemplateView.as_view(template_name="login.html"), name='login'), # NEWADD
    url(r'^logout/$', TemplateView.as_view(template_name="logout.html"), name='logout'), # NEWADD
    url(r'^password-reset/$', TemplateView.as_view(template_name="password_reset.html"), name='password-reset'), # NEWADD
    url(r'^password-reset/confirm/$', TemplateView.as_view(template_name="password_reset_confirm.html"), name='password-reset-confirm'), # NEWADD
    url(r'^user-details/$', TemplateView.as_view(template_name="user_details.html"), name='user-details'), # NEWADD
    url(r'^password-change/$', TemplateView.as_view(template_name="password_change.html"), name='password-change'), # NEWADD
    url(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,32})/$',  # NEWADD
        TemplateView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'), # NEWADD
    url(r'^dj-rest-auth/', include('dj_rest_auth.urls')), # NEWADD
    url(r'^dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), # NEWADD
    # https://dj-rest-auth.readthedocs.io/en/latest/api_endpoints.html
    path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'), # NEWADD
    url(r'^account/', include('allauth.urls')), # NEWADD
    url(settings.ADMIN_URL, admin.site.urls), # SPLITPOINT
    url(r'^accounts/profile/$', RedirectView.as_view(url='/', permanent=True), name='profile-redirect'), # NEWADD
    url(r'^docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='api_docs') # NEWADD

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


