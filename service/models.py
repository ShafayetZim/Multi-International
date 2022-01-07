from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    icon = models.ImageField(upload_to='service')

    def __str__(self):
        return self.title
