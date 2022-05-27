from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length = 100, null=False,blank=False)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Photo(models.Model):
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,blank=True)
    description=models.TextField(null=True)
    image = models.ImageField(default='DEFAULT VALUE')
    
    
    def __str__(self):
        return self.description

    @classmethod
    def update_image(cls, id, value):
        cls.o

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
        
    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images
