from django.db import models
from django.contrib.auth.models import User

INSTITUTION_TYPES = (
    (0, "fundacja"),
    (1, "organizacja pozarządowa"),
    (2, "zbiórka lokalna"),
)


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="nazwa")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Institution(models.Model):
    name = models.CharField(max_length=100, verbose_name="nazwa")
    description = models.TextField(verbose_name="opis")
    type = models.IntegerField(choices=INSTITUTION_TYPES, default=0, verbose_name="typ")
    categories = models.ManyToManyField(Category, verbose_name="kategorie")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Instytucja"
        verbose_name_plural = "Instytucje"


class Donation(models.Model):
    quantity = models.IntegerField(verbose_name="ilość worków")
    categories = models.ManyToManyField(Category, verbose_name="kategorie")
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=80, verbose_name="adres")
    phone_number = models.CharField(max_length=15, verbose_name="numer telefonu")
    zip_code = models.CharField(max_length=16, verbose_name="kod pocztowy")
    pick_up_date = models.DateField(verbose_name="data odbioru")
    pick_up_time = models.TimeField(verbose_name="czas odbioru")
    pick_up_comment = models.TextField(verbose_name="komentarz")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None, verbose_name="użytkownik")

    def __str__(self):
        return f'dotacja {self.user.username}: {self.quantity} worków dla {self.institution.name}'

    class Meta:
        verbose_name = "Dotacja"
        verbose_name_plural = "Dotacje"
