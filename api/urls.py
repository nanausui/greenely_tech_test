# coding: utf-8

from rest_framework import routers
from .views import DataViewSet, LimitViewSet


router = routers.DefaultRouter()
router.register(r'data', DataViewSet)
router.register(r'limit', LimitViewSet)