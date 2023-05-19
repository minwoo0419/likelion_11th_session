from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    
    def __str__(self):
        return self.name
    def delete_if_unused(self):
        if not self.posts.exists() and not self.comments.exists():
            self.delete()
            return 1
        return 0

class Post(models.Model):
    title = models.CharField(max_length=200)
    week = models.IntegerField(default=0)
    pub_date = models.DateTimeField()
    body = models.TextField()
    feel = models.TextField()
    image = models.ImageField(upload_to="post/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)
    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:30]

class Comment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='comments', blank=True)
    
    def __str__(self):
        return self.post.title + " : " + self.content[:20]