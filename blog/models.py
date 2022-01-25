from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from taggit.managers import TaggableManager
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default="default.png", upload_to="images/profile", null=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=CASCADE, related_name='posts')
    intro = models.TextField()
    image = models.ImageField(
        upload_to="images/profile", null=True)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    tags = TaggableManager()

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return f'{self.title} posted at {self.date_added}'

    def get_absolute_url(self):
        return reverse('blog:detail', args=(str(self.id)))


class Comment(models.Model):
    post = models.ForeignKey(
        "Post", related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)

    def __str__(self):
        return f'{self.name} commented on {self.post}'
