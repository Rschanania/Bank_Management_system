from django.shortcuts import render
from django.core.serializers import serialize
from branch.models import branches, BranchForm,banks
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist



from .serializers import BranchSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters import rest_framework as filters


class BranchFilter(FilterSet):
    
    ifsc=filters.CharFilter(method='filter_by_ifsc')
   
    class Meta:
        model=branches
        fields=['bank_id','city']
    

    def filter_by_ifsc(self,queryset,name,value):
        ifsc=value
        
        return queryset.filter(ifsc=ifsc)



        


class BranchViewSets(viewsets.ModelViewSet):
    queryset = branches.objects.all()
    serializer_class = BranchSerializer
    lookup_field='ifsc'
    filter_backends=(DjangoFilterBackend,)
    filter_class=BranchFilter
