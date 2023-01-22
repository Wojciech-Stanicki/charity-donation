from django.db import models
from django.contrib.auth.models import User

INSTITUTION_TYPES = (
    (0, "fundacja"),
    (1, "organizacja pozarządowa"),
    (2, "zbiórka lokalna"),
)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Institution(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.IntegerField(choices=INSTITUTION_TYPES, default=0)
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=16)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)

