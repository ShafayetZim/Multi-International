from django.db import models


class Contact(models.Model):
    location = models.CharField(max_length=200)
    mail1 = models.EmailField()
    mail2 = models.EmailField()
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
