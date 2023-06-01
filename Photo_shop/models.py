from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email= models.EmailField()
    subject=models.CharField(max_length=100)
    message= models.CharField(max_length=400)
    def __str__(self):
        return self.name
class Gallery(models.Model):
    tittle_no = models.AutoField
    category = models.CharField(max_length=30,default="General")
    image = models.ImageField()
    def __str__(self):
        return self.category
