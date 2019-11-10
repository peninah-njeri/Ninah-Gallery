from django.db import models

# Create your models here.
    
class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name




class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    

class Image(models.Model):
    image = models.ImageField(upload_to='images_folder')
    name = models.CharField(max_length =30)
    description = models.TextField(max_length=400)
    location = models.ForeignKey(Location, blank=True, null=True, on_delete=models.SET_NULL)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def get_all_images(cls):
        return cls.objects.all()

    @classmethod
    def filter_images_by_search(cls,search_term):
        return cls.objects.filter(category__title__icontains=search_term).all()





