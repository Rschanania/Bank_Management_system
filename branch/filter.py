import django_filters
from . models import branches as Branch

from django_filters import CharFilter




class BranchFilter(django_filters.FilterSet):

   
    branch=CharFilter(field_name='branch', lookup_expr='icontains')

    class Meta:
        model=Branch
        fields=['branch',]








class IfscFilter(django_filters.FilterSet):
    
   
    ifsc=CharFilter(field_name='ifsc', lookup_expr='exact')

    class Meta:
        model=Branch
        fields=['ifsc',]
    