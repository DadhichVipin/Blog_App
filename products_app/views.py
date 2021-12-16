from django.shortcuts import render

from products_app.models import Products


def index(request):
     products = Products.get_all_products()
     data = {}
     data['products'] = products
     return render(request, "index.html", data)
