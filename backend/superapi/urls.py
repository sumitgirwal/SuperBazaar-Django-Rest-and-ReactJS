from django.urls import path
from .views import ProductList, ProductDetail, OrderList, OrderDetail, UserSignUp, UserLogin

urlpatterns = [
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('orders/', OrderList.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    path('signup/', UserSignUp.as_view(), name='user_signup'),
    path('login/', UserLogin.as_view(), name='user_login'),
]