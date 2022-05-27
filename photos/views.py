from django.shortcuts import render
from django.http  import HttpResponse
from .models import Category,Photo

# Create your views here.
def gallery(request):
    #query a particular category
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name__contains=category)
    
    categories = Category.objects.all()
   

    context = {'categories':categories,'photos':photos}
    return render(request,'photos/gallery.html',context)

def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'photos/photo.html',{'photo':photo})

def search_results(request):

    if 'Category' in request.GET and request.GET["Category"]:
        search_term = request.GET.get("Category")
        searched_categories = Category.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})