import os

from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class File(models.Model):
    users = models.ManyToManyField(User, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    file = models.FileField(null=False, blank=False)
    date = models.DateTimeField(auto_now=True)

    def filename(self):
        return os.path.basename(self.file.name)

