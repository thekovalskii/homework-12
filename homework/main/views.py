from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .forms import ProductForm

# Create your views here.


def add_product(request: HttpRequest):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('a new product successfully created!')

    context = {
        'form': ProductForm
    }

    return render(request, 'add_product.html', context)
