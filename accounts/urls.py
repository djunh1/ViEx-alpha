from django.conf.urls import patterns, url


urlpatterns = [
    url(r'^login$', 'accounts.views.login', name='login'),
    url(r'^logout$', 'accounts.views.logout', name='logout'),
    #url(r'^(\d+)/',views.view_stocks,name='view_stocks'),
]