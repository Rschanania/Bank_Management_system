from django.urls import path,include
from .views import show,edit,delete,add,search

urlpatterns=[
    path('',show.as_view(),name="show"),
    path('add/',add.as_view(),name="bank-add"),
    path('edit/<slug:pk>/',edit.as_view(),name="bank-edit"),
    path('delete/<slug:pk>/',delete.as_view(),name="bank-delete"),
  
    path('search/',search,name="search"),
]