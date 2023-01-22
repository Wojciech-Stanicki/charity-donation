from django.shortcuts import render
from django.views import View
from django.db.models import Sum, Count
from .models import Donation


class LandingPage(View):
    def get(self, request):
        donated_bags = Donation.objects.aggregate(sum=Sum('quantity'))
        supported_institutions = Donation.objects.aggregate(count=Count('institution', distinct=True))
        ctx = {
            'donated_bags': donated_bags,
            'supported_institutions': supported_institutions,
        }
        return render(request, "giveaway/index.html", ctx)


class AddDonation(View):
    def get(self, request):
        return render(request, "giveaway/form.html")


class Login(View):
    def get(self, request):
        return render(request, "giveaway/login.html")


class Register(View):
    def get(self, request):
        return render(request, "giveaway/register.html")


class FormConfimation(View):
    def get(self, request):
        return render(request, "giveaway/form-confirmation.html")
