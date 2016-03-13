
from django.conf.urls import include, url, patterns
from django.contrib import admin

from rest_framework_nested import routers

from stockData import views as stock_views
from stockData import urls as stock_urls
from accounts import urls as account_urls
from accounts.views import UserViewSet

from superlists.views import IndexView
from accounts.views import LoginView
from accounts.views import LogoutView

from valueFact.views import ValueFactViewSet, AccountPostsViewSet


router=routers.SimpleRouter()

router.register(r'accounts', UserViewSet)
router.register(r'posts', ValueFactViewSet)

#Nest accounts to get results for a certtain accout.  Change this for certain stocks

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account')
accounts_router.register(r'posts', AccountPostsViewSet)

urlpatterns = [
    url(r'^$', stock_views.home_page, name='home'),
    #url(r'^stocks/',include(stock_urls)),
    url(r'^accounts/',include(account_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(accounts_router.urls)),
    url(r'^.*$', IndexView.as_view(), name='index'),
]
