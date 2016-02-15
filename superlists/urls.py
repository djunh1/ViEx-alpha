
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework_nested import routers

from stockData import views as stock_views
from stockData import urls as stock_urls
from accounts import urls as account_urls
from valueFact import urls as valueFact_urls

router=routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    url(r'^$', stock_views.home_page, name='home'),
    url(r'^stocks/',include(stock_urls)),
    url(r'^accounts/',include(account_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^valuefact/', include(valueFact_urls)),
    url(r'^api/v1/', include(router.urls)),
    url(r'^.*$', IndexView.as_view(), name='index'),
]
