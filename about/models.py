from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='about')
    shape = models.ImageField(upload_to='about')


class Vision(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='about/visions')

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='about/teams')

    def __str__(self):
        return self.name


class Choice(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.ImageField(upload_to='about')

