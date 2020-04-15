from django.urls import path,include
from . import views
from rest_framework import viewsets
from rest_framework.routers import DefaultRouter,SimpleRouter
from . views import BranchViewSets



route=DefaultRouter()
route.register('branches',BranchViewSets)

urlpatterns=[

    path('branches/',include(route.urls)),



]