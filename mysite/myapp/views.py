from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list
    }
    return render(request,"myapp/index.html",context)

def item(request):
    return HttpResponse("<h1>This is an item view</h1>")