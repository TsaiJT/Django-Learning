from django.http import Http404
from django.shortcuts import render

# Create your views here.
from .models import Product
from .forms import ProductForm, RawProductForm


def product_raw_view(request):

    init_data = {
        'title' : "My title"
    }

    my_form = RawProductForm(initial = init_data)

    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid(): # The data is good
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)

    #passing the form to the front-end.
    context = {
        'form' : my_form
    }

    return render(request, 'product/product_rawHTML_test.html', context)


def product_create_view(request):

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()

    context = {
        'form' : form
    }

    return render(request, 'product/product_create.html', context)


def product_detail_view(request):

    queryset = Product.objects.all()
    context = {
        'object_list' : queryset
    }

    # render(arg1, arg2, arg3)
    # arg1 -> handle the request
    # arg2 -> include the template path for the page
    # arg3 -> pass the context variable to html.
    return render(request, 'product/product_detail.html', context)


def product_lookup_view(request, id):
    try:
        obj = Product.objects.get(id = id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        'object' : obj
    }

    return render(request, 'product/product_lookup.html', context)