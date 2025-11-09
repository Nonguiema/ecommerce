from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
     path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('cart/', views.cart_view, name='cart_view'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
      path('dashboard/', views.dashboard, name='dashboard'),
      path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
path('delete/<int:product_id>/', views.delete_product, name='delete_product'),

path('dashboard/users/', views.dashboard_users, name='dashboard_users'),
path('dashboard/orders/', views.dashboard_orders, name='dashboard_orders'),
path('dashboard/products/', views.dashboard_products, name='dashboard_products'),
path('dashboard/sales/', views.dashboard_sales, name='dashboard_sales'),
 #path('dashboard/users/', views.users_list, name='users_list'),

]


