from django.urls import path
from . import views
from api.views import ProductsInventoryViewSet
app_name = "inventory"

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('new-product', views.NewProductView.as_view(), name='new-product'),
    path('new-product/success', views.success_view, name='success'),
    path('<pk>/update/', views.ProductDetail.as_view(), name='product-detail'),
    #path(r'^detail/(?P<pk>\d+)/$/', views.ProductDetail.as_view(), name='product-detail'),
    path('categories/', views.categories, name='categories'),
    path('category_add/', views.category_add, name='category-add'),
    path('category_update/', views.category_update, name='category-update'),
    path('category_delete/', views.category_delete, name='category-delete'),
    path('locations/', views.locations, name='locations'),
    path('location_add/', views.location_add, name='location-add'),
    path('location_update/', views.location_update, name='location-update'),
    path('location_delete/', views.location_delete, name='location-delete'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('supplier_add/', views.supplier_add, name='supplier-add'),
    path('supplier_update/', views.supplier_update, name='supplier-update'),
    path('supplier_delete/', views.supplier_delete, name='supplier-delete'),
    path('ajax-product-list/', views.ajax_products, name='ajax-product-list'),
    path('inventory/<int:location>', ProductsInventoryViewSet.as_view(), name='ajax-inventory')   
]

