import datetime

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .forms import ProductForm

# Create your views here.


def add_product(request: HttpRequest):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()

            expires_on = datetime.datetime.now() + datetime.timedelta(minutes=10)

            response = HttpResponse('a new product successfully created!')
            
            # пробач я реально не придумав нічого іншого
            response.set_cookie('kanye_did_smth_wrong', False, expires=expires_on)
            response.set_cookie('kanye_is_a_genius', True, expires=expires_on)

            return response

    context = {
        'form': ProductForm
    }

    return render(request, 'add_product.html', context)
