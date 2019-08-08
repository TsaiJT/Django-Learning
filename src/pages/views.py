from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request, *args, **kwargs):
    backend_data = {
        'my_text' : 'this is from back end',
        'my_number' : 66666,
        'my_list' : [123, 456, 789]
    }

    return render(request, 'home_page.html', backend_data)

def about_page(request, *args, **kwargs):
    return render(request, 'about_page.html') 

def contact_page(request, *args, **kwargs):
    return render(request, 'contact_page.html') 