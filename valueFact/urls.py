from django.conf.urls import url

from valueFact import views
from valueFact.feeds import LatestPostsFeed


urlpatterns = [

    url(r'^$',
        views.valueFactListView.as_view(),
        name='valueFact_list'),

    url(r'^(?P<year>\d{4})/(?P<post>[-\w]+)/$',
        views.valuefact_detail,
        name='valuefact_detail'),

    url(r'^(?P<fact_id>\d+)/share/$',
        views.valuefact_share,
        name='valuefact_share'),
    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),

]