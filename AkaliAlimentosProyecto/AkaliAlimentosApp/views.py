from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import *
from .forms import *

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

def cart(request):
    # ACA HAY QUE HACER QUE BUSQUE EL CARRITO DEL USUARIO
    return render(request, 'cart.html')

def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': True})
    else:
        return render(request, 'login.html')

def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
                if request.method == "POST":
                    form = NewProductForm(request.POST)
                    if form.is_valid():
                        data = form.cleaned_data
                        product = Product(name = data["name"], category = data["category"], nationality = data["nationality"], price = data["price"], stock = data["stock"], img = data["img"], short_description = data["short_description"], description = data["description"])
                        product.save()
                        return render(request, 'admindashboard.html')
                else:
                    form = NewProductForm()
                    return render(request, 'admindashboard.html')
        else:
            return render (request, 'userdashboard.html')
    else:
        return redirect('index')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            hashed_password = make_password(data["password"])
            user = User(username = data["username"], password = hashed_password,first_name = data["first_name"],last_name = data["last_name"],email = data["email"],address = data["address"])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
        return render(request, 'register.html',{"form": form})

def logoutview(request):
    logout(request)
    return redirect('index')