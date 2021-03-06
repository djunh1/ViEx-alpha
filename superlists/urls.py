from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from valueFact.sitemaps import PostSitemap
from valueFact import views as stockviews
from superlists import views as mainViews



admin.autodiscover()

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^companies/', include('valueFact.urls', namespace='companies', app_name='companies')),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url(r'^faq/', mainViews.faq, name='faq'),
    url(r'^toc/', mainViews.toc, name='toc'),
    url(r'^contact/', stockviews.contact, name='contact'),
    url('social-auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^$', stockviews.home_page, name='home_page'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
TO DO-

1- SITEMAPS, change the domain name for production from example.com to valueinvestingexchange.com

'''