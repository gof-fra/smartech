from django.shortcuts import render
from .models import Products

products = [
    {
        'code': '',
        'designation': 'hachim',
        'description': 'elv',
        'titre': 'IMB',
        'price': 'IBM Blog',
        'active': '21-02-2019',
    },
    {
        'code': '',
        'designation': 'hachim',
        'description': 'elv',
        'titre': 'IMB',
        'price': 'IBM Blog',
        'active': '21-02-2019',
    }
]


def listing(request):
    context = {
        'products': Products.objects.all()
    }
    return render(request, 'products/product.html', context)
