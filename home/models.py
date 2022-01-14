from django.db import models
from PIL import Image
from ckeditor.fields import RichTextField


# Create your models here.
class Base(models.Model):
    header_logo = models.ImageField(upload_to='pics')
    header_phone = models.CharField(max_length=20)
    footer_logo = models.ImageField(upload_to='pics')
    footer_intro = models.TextField()
    # types = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    telephone = models.IntegerField()
    mobile1 = models.IntegerField()
    mobile2 = models.IntegerField()
    quotes1 = models.TextField()
    quotes2 = models.TextField()

    # def __str__(self):
    #     return self.email


class Feature(models.Model):
    right_title = models.CharField(max_length=200)
    # description = models.TextField()
    description = RichTextField()
    icon = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.right_title


class WorkingProcess(models.Model):
    title = models.CharField(max_length=200)
    # description = models.TextField()
    description = RichTextField()

    def __str__(self):
        return self.title


class Slider(models.Model):
    image = models.ImageField(upload_to='slider')
