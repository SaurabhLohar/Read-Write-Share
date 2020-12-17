from django.db import models
from django.utils import timezone
from datetime import datetime

from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse




# Create your models here.

class Post(models.Model):

    options = (
    ('private','private'),
    ('public','public'),
    )

    title = models.CharField(blank=True, max_length=200)
    image = models.ImageField(upload_to='thumbnails/%Y/%m/%d/',default="default.png")
    slug = models.SlugField(max_length=250,unique=True,editable=False, null=True,blank=True)
    publish = models.DateTimeField(blank=True, default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    content = models.TextField(blank=True)
    status = models.CharField(choices=options,max_length=50)

    class Meta:
        ordering = ['-publish']

    # def get_absolute_url(self):
    #     return reverse('blog.views.single_post',args=[str(self.slug)])

    # def get_absolute_url(self):
    #     return reverse('blog.views.')


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_date(self):
        time = datetime.now()
        if self.publish.day == time.day:
            return str(time.hour - self.publish.hour) + " hours ago"
        else:
            if self.publish.month == time.month:
                return str(time.day - self.publish.day) + " day(s) ago"
            else:
                if self.publish.year == time.year:
                    return str(time.month - self.publish.month) + " months ago"
        return self.publish


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/',default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Profile'