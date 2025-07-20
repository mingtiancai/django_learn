# myapp/views.py
from django.shortcuts import render
from .forms import RegistrationForm
from . import models


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            models.Person.objects.create(id=10, name=name, email=email, password=password)
            return render(request, "myapp/success.html", {"name": name})
    else:
        form = RegistrationForm()

    return render(request, "myapp/register.html", {"form": form})
