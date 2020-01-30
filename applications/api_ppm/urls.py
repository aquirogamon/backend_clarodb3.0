from django.conf.urls import url
from django.urls import include, path
from applications.api_ppm import views
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Documentation API')

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)
router.register('internetInterfaces', views.internetInterfaceViewSet)
router.register('coreInterfaces', views.coreInterfaceViewSet)
router.register('peerTypes', views.PeerTypeViewSet)
router.register('serviceTypes', views.ServiceTypeViewSet)
router.register('services', views.ServiceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/docs/', schema_view),
]
