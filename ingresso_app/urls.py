from django.urls import path
from . import views
from .api.api import lugares

urlpatterns = [
    path('', views.hello_world, name='hello_world'),

    path('comprar_ingresso/', views.comprar_ingresso, name='comprar_ingresso'),
    path('lugares/', lugares, name='lugares'),
]