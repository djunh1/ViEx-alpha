from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from valueFact.sitemaps import PostSitemap


admin.autodiscover()

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^companies/', include('valueFact.urls', namespace='companies', app_name='companies')),
    url(r'^account/', include('accounts.urls')),
    url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


'''
TO DO-

1- SITEMAPS, change the domain name for production from example.com to valueinvestingexchange.com, or whatever it is

'''