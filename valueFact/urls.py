from django.conf.urls import url

from valueFact import views
from valueFact.feeds import LatestPostsFeed


urlpatterns = [

    url(r'^$',
        views.search_home,
        name='search_home'),

    url(r'^mine/$', views.ManagePostListView.as_view(),
        name='manage_post_list'),


    url(r'^(?P<symbol>[A-Za-z.-]{0,5})/$',
        views.view_stock,
        name='view_stock'),

    url(r'^create/(?P<symbol>[A-Za-z.-]{0,5})/$', views.PostCreateView.as_view(),
        name='post_create'),

    url(r'^(?P<stockticker>[A-Za-z.-]{0,5})/(?P<year>\d{4})/(?P<post>[-\w.]+)/$',
        views.valuefact_detail,
        name='valuefact_detail'),

    url(r'^(?P<fact_id>\d+)/share/$',
        views.valuefact_share,
        name='valuefact_share'),

    url(r'^feed/$', LatestPostsFeed(), name='post_feed'),

    url(r'^(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(),
        name='post_edit'),

    url(r'^(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(),
        name='post_delete')

]