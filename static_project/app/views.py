from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def hello(request):
    return HttpResponse("hello world")

def date(request,year,month,day):
    return HttpResponse(str(year)+'/'+str(month)+'/'+str(day))

def year(request,year):
    return render(request,"myyear.html")

def my_dict(request,year,month):
    return render(request,"myyear_dict.html",{'month':month})
