from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from applications.api_ppm import views

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('groups', views.GroupView)
router.register('internetInterfaces', views.internetInterfaceView)
router.register('coreInterfaces', views.coreInterfaceView)
router.register('peerTypes', views.PeerTypeView)
router.register('serviceTypes', views.ServiceTypeView)
router.register('services', views.ServiceView)

urlpatterns = [
    path('', include(router.urls)),
]
