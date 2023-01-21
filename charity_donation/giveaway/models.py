from django.db import models

INSTITUTION_TYPES = (
    (0, "fundacja"),
    (1, "organizacja pozarządowa"),
    (2, "zbiórka lokalna"),
)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Institution(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.IntegerField(choices=INSTITUTION_TYPES, default=0)
    categories = models.ManyToManyField(Category)
