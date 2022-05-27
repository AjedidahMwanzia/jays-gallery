from django.shortcuts import render
from django.http  import HttpResponse
from .models import Category,Photo
# Create your views here.
def gallery(request):
    categories = categories.objects.all()
    context = {'categories':categories}
    return render(request,'photos/gallery.html',context)

def viewPhoto(request,pk):
    return render(request,'photos/photo.html')

def addPhoto(request):
    return render(request,'photos/add.html')