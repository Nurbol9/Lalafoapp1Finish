from .models import Category, Product
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from .forms import ProductForm
from django.urls import reverse_lazy

class CategoryListView(ListView):
    queryset = Category.objects.all()
    context_object_name = ('categories')
    template_name = 'category_list.html'

class ProductLIstViews(ListView):
    queryset = Product.objects.all()
    context_object_name = ('products')
    template_name = 'product_list.html'

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    context_object_name = ('product')
    template_name = 'product_detail.html'


class ProductCreateView(CreateView):
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')


class ProductUpdateView(UpdateView):
    queryset = Product.objects.all()
    form_class = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')

