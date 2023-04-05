from django.urls import path
from . import views
app_name = "order"
urlpatterns = [
    path('', views.orders, name='orders'),
    path('create/', views.create_order, name='create-order'),
    path('create/cart/', views.create_order_cart, name='create-order-cart'),    
    path('create/checkout/', views.create_order_checkout, name='create-order-checkout'),
    path('create/checkout/thank-you/', views.order_thankyou, name='checkout-thank-you'),
    #path('update-cart-session/', views.update_cart_session, name='update-cart-session'),
]
