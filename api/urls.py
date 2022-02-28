# coding: utf-8
from django.urls import path, include
from .views import DataViewSet, LimitViewSet


urlpatterns = [
    path('data/', DataViewSet.as_view()),
    path('limit/', LimitViewSet.as_view()),
]