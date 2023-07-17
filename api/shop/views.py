from django.shortcuts import render
from django.http import JsonResponse
from E_commerce.settings import BASE_DIR
from .models import Product


def index(request):
    return render(request, 'index.html')


def ProductListView(request):
    products = Product.objects.all()
    route = f'/static/img/'
    data = {
        'products': [
            {
                'name': product.product_name,
                'price': product.price,
                'slug': product.slug,
                'stock': product.stock,
                'description': product.description,
                'thumbnail': f'{product.thumbnail.name[6:]}',
            }
            for product in products
        ]
    }

    return JsonResponse(data)
