from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about_view, name='about'),
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/<int:food_id>/', views.add_to_cart, name='add_to_cart'),
    path('increase-cart-item/<int:item_id>/', views.increase_cart_item, name='increase_cart_item'),
    path('decrease-cart-item/<int:item_id>/', views.decrease_cart_item, name='decrease_cart_item'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-history/', views.order_history_view, name='order_history'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation_view, name='order_confirmation'),
]

