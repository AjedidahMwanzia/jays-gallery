from django.shortcuts import render
from django.http  import HttpResponse
from .models import Category,Photo,Location

# Create your views here.
def gallery(request):
    #query a particular category
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name__contains=category)
    
    categories = Category.objects.all()
    locations=Location.objects.all

    context = {'categories':categories,'photos':photos,'locations':locations}
    return render(request,'photos/gallery.html',context)

def viewPhoto(request,pk):
    photo = Photo.objects.get(id=pk)
    return render(request,'photos/photo.html',{'photo':photo})

def search_results(request):

    if 'name' in request.GET and request.GET["name"]:
        search_term = request.GET.get("name")
        searched_photos = Photo.search_photo(search_term)
        print(searched_photos)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"images": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})

def get_location(request,location_id):
    photos=Photo.filter_by_location(location_id)

    return render (request,'photos/location.html',{'photos':photo})