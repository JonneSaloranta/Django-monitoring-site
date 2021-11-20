from django.shortcuts import render


from .forms import PostCreateForm, RawPostForm
from .models import PostModel


def post_create_form(request):
    my_form = RawPostForm(request.POST)
    context = {"form": my_form}
    return render(request, "products/product_create.html", context)
