from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, FormView

from apps.forms import RegisterForm
from apps.models import Product, Category, Cart


# Create your views here.

class ProductListView(ListView):
    queryset= Product.objects.all()
    context_object_name = 'products'
    template_name = 'apps/product_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(object_list=object_list, **kwargs)
        data['categories'] = Category.objects.all()
        return data

    def get_queryset(self):
        query = super().get_queryset()
        cat_slug = self.request.GET.get("category")
        if cat_slug:
            query = query.filter(category__slug=cat_slug)
        return query


class RegisterFormView(FormView):
    template_name = 'apps/auth/register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return redirect('login')

class CartListView(ListView):
    queryset = Cart.objects.all()
    context_object_name = 'carts'
    template_name = 'apps/cart_list.html'


class CartDeleteView(View):
    def get(self, request, pk):
        Cart.objects.filter(pk=pk).first().delete()
        return redirect('carts')
