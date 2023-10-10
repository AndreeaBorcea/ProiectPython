from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView

from product.forms import ContactRequestForm, ClientForm
from product.models import *


def homepage_view(request):
    products = Product.objects.order_by('-id')[:min(3, Product.objects.count())]
    # categories = Category.objects.all()
    return render(request, "homepage.html", {'products': products})


# class ProductListView(LoginRequiredMixin, ListView):
class ProductListView(ListView):
    model = Product
    template_name = 'all_products.html'
    context_object_name = 'products'

    # queryset = Product.objects.all()

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        return Product.objects.filter(Q(name__icontains=q) | Q(description__icontains=q))


class CategoryDetailView(DetailView):
    model = Category  # modelul de care se ocupa
    template_name = 'category_detail.html'  # template-ul pe care il incarca
    context_object_name = 'category'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


@login_required
def get_open_cart(request):
    open_cart = Cart.objects.filter(user=request.user, status='open').first()
    if open_cart is None:
        open_cart = Cart.objects.create(user=request.user, status='open')
    return open_cart


@login_required
def open_cart_view(request):
    open_cart = get_open_cart(request)
    return render(request, 'open_cart.html', {'cart': open_cart})


@login_required
def add_product_to_cart(request):
    open_cart = get_open_cart(request)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity', 1)
        cart_item = CartItem.objects.filter(cart=open_cart, product_id=product_id).first()
        if cart_item is None:
            cart_item = CartItem.objects.create(cart=open_cart, product_id=product_id, quantity=quantity)
        else:
            cart_item.quantity += int(quantity)
            cart_item.save()
        if int(cart_item.quantity) < 1:
            cart_item.delete()
        # return redirect(reverse_lazy('open_cart'))
        return redirect(request.META['HTTP_REFERER'])


class ContactRequestCreateView(CreateView):
    model = ContactRequest
    form_class = ContactRequestForm
    template_name = 'contact_request_create.html'
    success_url = reverse_lazy('homepage')


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_create.html'
    success_url = reverse_lazy('login')
