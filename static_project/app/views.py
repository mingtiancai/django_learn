from django.shortcuts import render
from django.http import HttpResponse
import csv
from . import models

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

def download(request):
    response=HttpResponse(content_type="text/csv")
    response['Content-Disposition']='attachment;filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row','A','B','C'])
    return response

def google(request):
    return render(request,"Google.html")

def get_data(request):
    print("----------------------")
    items = models.Product.objects.all()
    print(items)
    # return render(request,"myyear.html")
    return render(request, 'database.html', {'items': items})
