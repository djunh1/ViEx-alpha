from django.conf.urls import include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^companies/', include('valueFact.urls', namespace='companies', app_name='companies')),

]
