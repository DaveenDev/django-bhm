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
    path('locations/', views.locations, name='locations'),
    path('categories/', views.categories, name='categories'),
    path('suppliers/', views.suppliers, name='suppliers'),
    path('ajax-product-list/', views.ajax_products, name='ajax-product-list'),
    path('inventory/<int:location>', ProductsInventoryViewSet.as_view(), name='ajax-inventory')   
]

