
from django.conf.urls import include, url, patterns
from django.contrib import admin

from rest_framework_nested import routers


from accounts.views import UserViewSet


from superlists.views import IndexView
from accounts.views import LoginView
from accounts.views import LogoutView

from valueFact.views import ValueFactViewSet, AccountPostsViewSet

admin.autodiscover()
router=routers.SimpleRouter()

router.register(r'accounts', UserViewSet)
router.register(r'posts', ValueFactViewSet)

admin.autodiscover()


accounts_router = routers.NestedSimpleRouter(router, r'accounts', lookup='account')
accounts_router.register(r'posts', AccountPostsViewSet)

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^.*$', IndexView.as_view(), name='index'),
]
