from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User   # Default users


class Post(models.Model):
    objects = None

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  # auto_now_add will add the date only when it is created
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # if a user is deleted then his post will be deleted as well

    def __str__(self):
        return self.title
