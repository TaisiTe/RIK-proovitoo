from django.urls import path
from companies.views import CompanyCreateView, CompanyUpdateView, CompanyDetailView, CompanySearchView

urlpatterns = [
    path('', CompanySearchView.as_view(), name='home'),
    path('create/', CompanyCreateView.as_view(), name='create'),
    path('company/<int:reg_code>/', CompanyDetailView.as_view(), name='details'),
    path('edit/<int:pk>/', CompanyUpdateView.as_view(), name='edit'),
]
