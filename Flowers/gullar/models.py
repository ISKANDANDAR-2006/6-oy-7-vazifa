
from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tur nomi")

    def __str__(self):
        return self.name

class Flower(models.Model):
    name = models.CharField(max_length=100, verbose_name="Gul nomi")
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="flowers", verbose_name="Turi")
    description = models.TextField(blank=True, verbose_name="Tavsif")

    def __str__(self):
        return self.name
