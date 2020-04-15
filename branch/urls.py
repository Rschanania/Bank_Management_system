from django.urls import path,include
from .views import show,edit,delete,add,branchFilter,search

urlpatterns=[
    path('',show.as_view(),name="show"),
    path('add/',add.as_view(),name="bank-add"),
    path('edit/<int:pk>/',edit.as_view(),name="bank-edit"),
    path('delete/<int:pk>/',delete.as_view(),name="bank-delete"),
    path('filter/',branchFilter,name="bank-filter"),
    path('search/',search,name="search"),
]