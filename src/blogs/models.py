from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)  # optional

    def __str__(self):
        """
        :return: La representación de un objeto como un string
        """
        return self.name


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=150)
    intro = models.CharField(max_length=350)
    body = models.TextField()
    image = models.FileField(null=True, blank=True)
    publish_date = models.DateField()
    categories = models.ManyToManyField(Category)

    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación del registro
    modified_at = models.DateTimeField(auto_now=True)  # Graba la fecha de la última modificación