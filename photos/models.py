from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length = 100, null=False,blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    description=models.CharField(max_length = 500, null=False,blank=False)
    image = models.ImageField(null=False, blank=False)
    Category=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description