from django.urls import path, include
from api import views
from api.views import CustomerListView, CustomerDetailView, MobileCompanyDetailView, MobileCompanyListView

urlpatterns = [
    path('customer/',CustomerListView.as_view(),name='CustomerListView'),
    path('customer/<int:pk>',CustomerDetailView.as_view(),name='CustomerDetailView'),
    path('company/',MobileCompanyListView.as_view(),name='MobileCompanyListView'),
    path('company/<int:pk>',MobileCompanyDetailView.as_view(),name='MobileCompanyDetailView'),
]





