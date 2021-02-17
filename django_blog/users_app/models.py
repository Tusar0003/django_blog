from django.db import models

# Create your models here.


class Userapp(models.Model):
    name = models.TextField(null=True)