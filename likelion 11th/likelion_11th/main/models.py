from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    week = models.IntegerField(default=0)
    pub_date = models.DateTimeField()
    body = models.TextField()
    feel = models.TextField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:30]