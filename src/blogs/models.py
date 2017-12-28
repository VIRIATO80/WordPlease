from django.contrib.auth.models import User
from django.db import models


class BlogPersonal(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    nombre_usuario = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    blog_name = models.CharField(max_length=150)
    blog_description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación del registro
    modified_at = models.DateTimeField(auto_now=True)  # Graba la fecha de la última modificación

    def __str__(self):
        """
        :return: La representación de un objeto como un string
        """
        return self.nombre_usuario

class Post(models.Model):

    blog = models.ForeignKey(BlogPersonal, on_delete=models.PROTECT)

    title = models.CharField(max_length=150)
    intro = models.CharField(max_length=350)
    body = models.TextField()
    image = models.FileField()

