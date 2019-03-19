from django.urls import path
from . import views


urlpatterns = [

    path('', views.Nosformation, name="formation-index")

]

