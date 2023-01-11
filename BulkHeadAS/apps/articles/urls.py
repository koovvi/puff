from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('myaccount/', views.MyAccountView.as_view(), name='myaccount'),
    path('catalog/', views.catalog, name='catalog'),
    path('order/', views.uploadFlower, name='addFlower')
    ]