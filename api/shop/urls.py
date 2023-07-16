from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('api/products/', views.ProductListView, name='product_list'),
]
