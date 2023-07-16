from django.shortcuts import render
from django.http import JsonResponse
from .models import Product


def index(request):
    return render(request, 'index.html')


def ProductListView(request):
    products = Product.objects.all()
    data = {
        'products': [
            {
                'name': product.name,
                'price': product.price,
                # Autres informations sur le produit
            }
            for product in products
        ]
    }
    return JsonResponse(data)
