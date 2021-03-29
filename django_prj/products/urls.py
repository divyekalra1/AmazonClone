from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('add/',views.newProduct,name='new-product'),
    path('update/<int:pk>',views.updateProduct,name='update-product'),
    path('details/<int:pk>',views.detailProduct,name='detail-product'),

]
