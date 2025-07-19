from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models

# Create your views here.

def test(request):
    models.Type.objects.create(id=10, type_name="asa")
    print(models.Type.objects.all())
    return HttpResponse("hello world")
