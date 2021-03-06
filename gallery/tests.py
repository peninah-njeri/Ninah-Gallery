from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.


class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image_1= Image(name = 'Jlo', description ='details')


    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image_1,Image))



     # Testing Save Method
    def test_save_method(self):
        self.image_1.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)


    
     # Testing Delete Method
    def test_delete_method(self):
        self.image_1.delete_image()
        images = Image.objects.all().delete()
        self.assertFalse(len(images) == 0)
    


class CategoryTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.adele= Category(title = 'female-musicians')

      # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.adele,Category))   

    # Testing Save Method
    def test_save_method(self):
        self.adele.save_title()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)    
         




class LocationTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.canada= Location(name = 'country')


    
      # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.canada,Location)) 


    # Testing Save Method
    def test_save_method(self):
        self.canada.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)  


   
     
