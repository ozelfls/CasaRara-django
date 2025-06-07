from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=150, unique=True)
    senha = models.CharField(max_length=64)

    def __str__(self):
        return self.username

