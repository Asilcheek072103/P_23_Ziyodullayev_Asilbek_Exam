from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps.views import ProductListView, RegisterFormView, CartListView, CartDeleteView

urlpatterns = [
    path('', ProductListView.as_view(), name = 'product_list'),
    path('login', LoginView.as_view(template_name = 'apps/auth/login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name = 'apps/auth/login.html'), name='logout'),
    path('register', RegisterFormView.as_view(), name='register'),
    path('carts', CartListView.as_view(), name='carts'),
    path('carts_delete/<int:pk>', CartDeleteView.as_view(), name='carts-delete'),

]