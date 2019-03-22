from django.urls import path
from . import views


urlpatterns = [

    path('', views.Nosformation, name='formation-index'),
    path('create/', views.create, name='create'),
    path('add/', views.add, name='edd-formation'),
    path('edit/<id>/', views.edit, name='edit'),
    path('delete/<id>/', views.delete, name='delete'),
    path('update/<id>/', views.update, name='update'),

]

