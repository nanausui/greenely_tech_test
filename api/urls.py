# coding: utf-8
from django.urls import path, include
from .views import DataViewSet


urlpatterns = [
    path('data/', DataViewSet.as_view()),
]