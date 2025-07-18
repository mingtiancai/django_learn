from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from django.http import HttpResponse

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

def test(request):
    return HttpResponse("hello world")

def res_func(request):
    print("----------")
    return HttpResponse("hello world")
