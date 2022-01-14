from django.db import models
from ckeditor.fields import RichTextField


class Service(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    icon = models.ImageField(upload_to='service')

    def __str__(self):
        return self.title

