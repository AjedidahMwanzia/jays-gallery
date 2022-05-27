from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=50)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def get_locations(cls):
        return Location.objects.all()

    @classmethod
    def update_location(cls,id,value):
        cls.objects.filter(id=id).update(name=value)

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length = 100, null=False,blank=False)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Photo(models.Model):
    name = models.CharField(max_length = 60)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,blank=True)
    description=models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='DEFAULT VALUE')
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(pk=id).update(image=value)
    
    @classmethod
    def filter_by_location(cls,location):
        img_location = Photo.objects.filter(location__name=location).all()
        return img_location

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
        
    @classmethod
    def get_image_by_id(cls,id):
        image = Photo.objects.filter(id=id).all()
        return image
        
    @classmethod
    def search_by_category(cls, search_term):
        photos = cls.objects.filter(category__name__icontains=search_term)
        return photos
