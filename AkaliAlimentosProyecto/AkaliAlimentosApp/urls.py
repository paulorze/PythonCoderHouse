from django.urls import path
from AkaliAlimentosApp import views
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name = 'about'),
    path('store', views.store, name = 'store'),
    path('contact', views.contact, name = 'contact'),
    path('cart', views.cartView.as_view(), name = 'cart'),
    path('login', views.loginview, name = 'login'),
    path('register', views.register, name = 'register'),
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('manageCart', views.manageCart, name = 'managecart'),
    
    #CLASS BASED VIEWS
    #PRODUCTS
    path('productDetail/<pk>', views.detailProduct.as_view(), name = "productDetail"),
    path('newProduct', views.newProduct.as_view(), name = 'productNew'),
    path('updateProduct/<pk>', views.updateProduct.as_view(), name = 'productUpdate'),
    path('deleteProduct/<pk>', views.deleteProduct.as_view(), name = 'productDelete'),
    
    #USER
    path('updateUser', views.updateUser, name = 'userUpdate'),
    path('updatePassword', views.updatePassword.as_view(), name = 'passwordUpdate'),
    
    #CART
    path('cart/deleteProduct/<pk>', views.cartDelete.as_view(), name = 'cartDelete'),
    
    #ORDERS
    path('cart/checkout', views.checkoutView.as_view(), name = 'checkout'),
    path('orders', views.ordersList.as_view(), name = 'orders')
]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)