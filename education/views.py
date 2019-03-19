from django.shortcuts import render
from .models import Formation


def Nosformation(request):
    return render(request, 'education/formation.html')
