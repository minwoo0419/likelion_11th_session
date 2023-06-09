from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.TextField(max_length=10)
    department = models.TextField(null=True, max_length=30)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    followings = models.ManyToManyField("self", related_name="followers", symmetrical=False, blank=True)

