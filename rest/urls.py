from django.conf.urls import url, include  # include
# from django.conf.urls.static import static
import oauth2_provider.views as oauth2_views
from rest_framework import routers
from rest.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


app_name="rest"


oauth2_endpoint_views = [
    url(r'^authorize/$',
        oauth2_views.AuthorizationView.as_view(), name="authorize"),
    url(r'^token/$', oauth2_views.TokenView.as_view(), name="token"),
    url(r'^revoke-token/$',
        oauth2_views.RevokeTokenView.as_view(), name="revoke-token"),
]


urlpatterns = [
    url(r'^auth/', include(oauth2_endpoint_views, None)),
    url(r'^', include(router.urls)),
]
