from django.urls import path, include
from rest_framework import routers
from . import views
app_name = "api"

router = routers.DefaultRouter()
router.register('products', views.ProductsViewSet)
router.register('categories', views.CategoriesViewSet)
router.register('units', views.UnitsViewSet)
router.register('orders',views.OrdersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('customers/', views.api_customers,name='api-customers'),
    path('customers/<int:id>/', views.api_customer,name='api-customer'),
    path('inventory/<int:location>',views.ProductsInventoryViewSet.as_view(), name='api-inventory')   
]

