from .models import *
from .forms import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def store(request):
    searchterm = request.GET.get("searchterm")
    if searchterm:
        products = Product.objects.filter(name__icontains = searchterm)
    else:
        products = Product.objects.all()
    return render(request, 'store.html',{"products": products})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            contact = Contact(name=data["name"], email=data["email"], body=data["body"])
            contact.save()
            return render(request, 'index.html')
    else:
        form = ContactForm()
        return render(request, 'contact.html',{"form": form})

def dashboard(request):
    if request.user.is_authenticated:
        return render (request, 'userdashboard.html')
    else:
        return redirect('index')

def loginview(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': True})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            hashed_password = make_password(data["password"])
            user = User(username = data["username"], password = hashed_password,first_name = data["first_name"],last_name = data["last_name"],email = data["email"],address = data["address"])
            user.save()
            cart = Cart.objects.create(user = user)
            cart.save()
            return redirect('login')
    else:
        form = RegisterForm()
        return render(request, 'register.html',{"form": form})

def logoutview(request):
    logout(request)
    return redirect('index')

def updateUser(request):
    user = request.user
    avatar, created = Avatar.objects.get_or_create(user=user)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance = request.user)
        if form.is_valid():
            if form.cleaned_data.get('img'):
                avatar.img = form.cleaned_data.get('img')
                avatar.save()
            form.save()
            return render (request, 'userdashboard.html')
    else:
        form = UserUpdateForm(instance = request.user)
    return render(request, 'userupdate.html', {'form': form})

class updatePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = "passwordupdate.html"
    success_url = reverse_lazy('dashboard')

class detailProduct (DetailView):
    model = Product
    template_name = 'productdetail.html'

class newProduct (UserPassesTestMixin, CreateView):
    model = Product
    template_name = "productnew.html"
    success_url = reverse_lazy('store')
    fields = ('name', 'category', 'short_description', 'description', 'price', 'stock', 'nationality', 'img')
    login_url = reverse_lazy('login')
    login_redirect = reverse_lazy('index')
    
    def test_func(self):
        user = self.request.user
        return user.is_authenticated
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect(self.login_redirect)
        else:
            return redirect(self.login_url)

class updateProduct (UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'productupdate.html'
    success_url = reverse_lazy('store')
    fields = ('name', 'category', 'short_description', 'description', 'price', 'stock', 'nationality', 'img')
    login_url = reverse_lazy('login')
    login_redirect = reverse_lazy('index')
    
    def test_func(self):
        user = self.request.user
        if not user.is_authenticated:
            return False 
        return user.is_superuser
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect(self.login_redirect)
        else:
            return redirect(self.login_url)

class deleteProduct (UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'productdelete.html'
    success_url = reverse_lazy('store')
    login_url = reverse_lazy('login')
    login_redirect = reverse_lazy('index')
    
    def test_func(self):
        user = self.request.user
        if not user.is_authenticated:
            return False 
        return user.is_superuser
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect(self.login_redirect)
        else:
            return redirect(self.login_url)

class cartView(LoginRequiredMixin, DetailView):
    model = Cart
    context_object_name = 'cart'
    template_name = 'cart.html'
    login_url = reverse_lazy('login')
    
    def get_object(self, queryset=None):
        return Cart.objects.get(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.object
        cart_items = cart.productlist.all()
        cart.total =0
        for cart_item in cart_items:
            cart.total += cart_item.calculate_subtotal()
        return context

def manageCart(request):
    if request.method == 'POST':
        user = request.user
        cart, create = Cart.objects.get_or_create(user=user)
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']
        try:
            product = Product.objects.get(pk=product_id)
            cart_item = CartToProduct.objects.get(cart = cart, product = product)
            cart_item.quantity = quantity
            cart_item.save()
            cart.productlist.add(cart_item)
            response_data = {'message': 'Ahora tienes: ' + quantity + ' unidad(es) en tu carrito ✔', 'success': True}
        except CartToProduct.DoesNotExist:
            cart_item = CartToProduct.objects.create(cart = cart, product = product, quantity = quantity)
            cart_item.save()
            cart.productlist.add(cart_item)
            response_data = {'message': 'Ahora tienes: ' + quantity + 'unidad(es) en tu carrito ✔', 'success': True}
        except:
            response_data = {'message': 'Ocurrió un error', 'success': False}
        return JsonResponse(response_data)

class cartDelete (LoginRequiredMixin, DeleteView):
    model = CartToProduct
    success_url = reverse_lazy('cart')
    login_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response_data = {}
        cart_item = False
        try:
            cart_item = CartToProduct.objects.get(pk=self.kwargs['pk'])
        except self.model.DoesNotExist:
            response_data = {'message': 'Ha ocurrido un error.', 'success': False}
            return JsonResponse(response_data)
        if self.request.user.cart.productlist.filter(pk=self.kwargs['pk']).exists():
            cart_item.delete()
            response_data = {'message': 'Producto eliminado con exito.', 'success': True}
        else:
            response_data = {'message': 'Ha ocurrido un error.', 'success': False}
        return JsonResponse(response_data)

class checkoutView(View):
    def post(self, request, *args, **kwargs):
        user = request.user
        cart, create = Cart.objects.get_or_create(user=user)
        total = 0
        for cart_item in cart.productlist.all():
            total += cart_item.product.price * cart_item.quantity
        order = Order.objects.create(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            address=user.address,
            total = total
        )
        for cart_item in cart.productlist.all():
            OrderToProduct.objects.create(
                order=order,
                product_name = cart_item.product.name,
                product_price = cart_item.product.price,
                quantity = cart_item.quantity,
                subtotal = cart_item.product.price * cart_item.quantity
            )
        cart.productlist.clear()
        return redirect('index')

class ordersList (LoginRequiredMixin,ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders.html'
    login_url = reverse_lazy('login')
    
    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Order.objects.none()
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(username=user.username)