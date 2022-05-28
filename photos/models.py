from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length = 100, null=False,blank=False)

    def __str__(self):
        return self.name

    def get_all_category(cls):
        categories = Category.objects.all()
        return categories

class Photo(models.Model):
    name = models.CharField(max_length =30,null=True)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True,blank=True)
    description=models.TextField(null=True)
    image = models.ImageField(default='DEFAULT VALUE')
    
    
    def __str__(self):
        return self.description

    def save_image(self):
        self.save()
    # delete the image database
    def delete_image(self):
        self.delete()
    # get all images
    @classmethod
    def get_all_images(cls):
        images = Photo.objects.all()
        return images
    

    # get image by id
    @classmethod
    def get_image_by_id(cls, id):
        image = Photo.objects.get(id=id)
        return image

    @classmethod
    def filter_by_category(cls, category_id):
        images = Photo.objects.filter(category_id=category_id)
        return images

    @classmethod
    def search_image(cls, search_term):
        images = cls.objects.filter(name__icontains=search_term)
        return images