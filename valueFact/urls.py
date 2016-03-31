from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^$', views.valueFactListView.as_view(), name='valueFact_list'),
    url(r'^(?P<year>\d{4})/(?P<post>[-\w]+)/$',
        views.valuefact_detail,
        name='valuefact_detail'),

]