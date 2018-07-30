from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    headline = models.CharField(max_length=500, null=False)
    content = models.TextField()
    publisher = models.ForeignKey(
        'auth.User', on_delete=models.DO_NOTHING, default=0)
    is_draft = models.BooleanField(default=True)
    date_published = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    picture = models.ImageField(
        upload_to='publisher_image', default="/upload3.jpeg")

    def __str__(self):
        """Return a human readable representation of the post model"""
        return self.title

    def get_absolute_url(self):
        """returns the URL to the detail view for the model"""
        return reverse('posts: post-detail', kwargs={'post_id': self.id})
