from django.urls import path, include
from rest_framework import routers
from . import views
app_name = "api"

router = routers.DefaultRouter()
router.register('products', views.ProductsViewSet)
#router.register(r'products/update/inventory', views.UpdateInventoryViewSet, basename="update-inventory")
router.register('categories', views.CategoriesViewSet)
router.register('units', views.UnitsViewSet)
router.register('orders',views.OrdersViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('products/update-inventory/<int:product_id>/', views.UpdateInventoryViewSet.as_view(), name="update-inventory"),
    path('inventory/<int:location_id>', views.ProductsInventoryViewSet.as_view(), name='api-inventory'), 
    path('customers/', views.api_customers,name='api-customers'),
    path('customers/<int:id>/', views.api_customer,name='api-customer'),
]

