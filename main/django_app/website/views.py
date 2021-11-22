from abc import abstractmethod
from django.shortcuts import render

from .forms import ProductCreateForm, RawProductForm
from .models import Product


def index(request):
    return render(request, "index.html", {})


def settings(request):
    return render(request, "settings.html", {})


def contact(request):
    context = {}
    return render(request, "contact.html")


def product_details(request):
    obj = Product.objects.get(id=3)
    context = {"object": obj}
    return render(request, "products/detail.html", context)


def product_create(request):
    my_form = RawProductForm(request.POST)
    context = {"form": my_form}
    return render(request, "products/product_create.html", context)
