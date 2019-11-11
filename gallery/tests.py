from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.

class CategoryTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.adele= Category(title = 'female-musicians')



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
    




