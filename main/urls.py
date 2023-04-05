from django.urls import path
from . import views
app_name = "main"

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('customers/', views.customers, name='customers'),
    path('customer/create/', views.create_customer, name='create-customer'),
    path('returns/', views.returns, name='returns'),
    path('return/create/', views.create_return, name='create-return')
]
