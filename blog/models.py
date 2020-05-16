from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, 
                            unique = True)
    author = models.ForeignKey(User,
                               related_name='blog_posts', on_delete=models.CASCADE)
    audio = models.URLField(max_length = 200, default = "spotify:episode:0Vbl7RvX3KE0lSkRmy9Wjj") 
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, 
                              choices=STATUS_CHOICES,
                              default='draft')
    post_Img = models.ImageField(default = 'test.jpg') 

    def get_absolute_url(self):
        return reverse('detail-post', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


