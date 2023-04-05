from django.urls import path
from . import views
app_name = "inventory"

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('locations/', views.locations, name='locations'),
    path('categories/', views.categories, name='categories'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('ajax-product-list/', views.ajax_products, name='ajax-product-list')
]
