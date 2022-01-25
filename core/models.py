from django.db import models


# Create your models here.
class About(models.Model):
    Content = models.TextField(max_length=600)
    Image = models.ImageField(upload_to='images', null=True)


class Offers(models.Model):
    title = models.CharField(max_length=100)
    Icons = models.TextField(max_length=200)
    Content = models.TextField(max_length=600)


class Teams(models.Model):
    image = models.ImageField(upload_to='team')
    Name = models.CharField(max_length=100)
    Title = models.TextField(max_length=200)
    description = models.TextField(max_length=600)


class Contact(models.Model):
    Email = models.EmailField(max_length=100)
    Subject = models.CharField(max_length=200)
    Body = models.TextField(max_length=600)
