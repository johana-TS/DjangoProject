from django.urls import path
from . import views #misma carpeta coloco un punto como referencia
urlpatters =[
    path('', views.hello)
]