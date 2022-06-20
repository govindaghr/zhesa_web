from django.conf.urls import url, include
from .views import  AllWordViewSet, PhelkayWordViewSet, ZhebsaPhelkayViewSet, ZhebsaWordViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("zhebsa", ZhebsaWordViewSet, basename="zhebsa")
router.register("phelkay", PhelkayWordViewSet, basename="phelkay")
router.register("zhesaphelkay", ZhebsaPhelkayViewSet, basename="zhesaphelkay")
router.register("allwords", AllWordViewSet, basename="allwords")

urlpatterns = [
    url('',include(router.urls))
]