from django.conf.urls import url

from valueFact import views
from valueFact.feeds import LatestPostsFeed


urlpatterns = [

    url(r'^$',
        views.search_home,
        name='search_home'),

    url(r'^(?P<symbol>[A-Za-z.-]{0,5})/$',
        views.view_stock,
        name='view_stock'),

    url(r'^(?P<year>\d{4})/(?P<post>[-\w]+)/$',
        views.valuefact_detail,
        name='valuefact_detail'),

    url(r'^(?P<fact_id>\d+)/share/$',
        views.valuefact_share,
        name='valuefact_share'),
    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),

]