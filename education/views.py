from django.shortcuts import render, redirect
from .models import Formation


def Nosformation(request):
    catal = Formation.objects.all()
    return render(request, 'education/formation.html', {'catals': catal})


def create(request):
    print(request.POST)
    description = request.GET['description']
    encadrant = request.GET['encadrant']
    date = request.GET['date']
    catal_detail = Formation(description=description, encadrant=encadrant, date=date, fichier=fichier)
    catal_detail.save()
    return redirect('/')


def add(request):
    return render(request, 'education/edit.html')


def edit(request, id):
    catals = Formation.objects.get(pk=id)
    context = {
        'catals': catals
    }
    return render(request, 'education/edit.html', context)


def delete(request):
    catals = Formation.objects.get(pk=id)
    catals.delete()
    return render(request, 'education/formation.html')
#   return redirect('home/')


def update(request, id):
    catals = Formation.objects.get(pk=id)
    catals.description = request.GET['description']
    catals.encadrant = request.GET['encadrant']
    catals.date = request.GET['date']
    catals.save()
    return redirect('/')
