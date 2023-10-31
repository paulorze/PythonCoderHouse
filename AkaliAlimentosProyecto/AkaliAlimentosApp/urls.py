from django.urls import path
from AkaliAlimentosApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name = 'about'),
    path('store', views.store, name = 'store'),
    path('contact', views.contact, name = 'contact'),
    path('cart', views.cart, name = 'cart'),
    path('login', views.loginview, name = 'login'),
    path('register', views.register, name = 'register'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('logout', views.logoutview, name = 'logout')
]