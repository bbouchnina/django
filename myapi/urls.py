from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from . import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
# router.register(r'clients', views.ClientViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    url(
        r'^api/clients/$',
        views.ClientViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='clients-list',
    ),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    # path('clients',views.ClientViewSet.as_view({'get': 'list', 'post': 'create'}))
]