from django.urls import path
from AkaliAlimentosApp import views

urlpatterns = [
    path('', views.index, name='index')
]