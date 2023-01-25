from django.shortcuts import render
from django.views import View
from django.db.models import Sum, Count
from .models import Donation, Institution


class LandingPage(View):
    def get(self, request):
        donated_bags = Donation.objects.aggregate(sum=Sum('quantity'))
        supported_institutions = Donation.objects.aggregate(count=Count('institution', distinct=True))
        foundations = Institution.objects.filter(type=0)
        non_governmental_organizations = Institution.objects.filter(type=1)
        community_collections = Institution.objects.filter(type=2)
        ctx = {
            'donated_bags': donated_bags,
            'supported_institutions': supported_institutions,
            'foundations': foundations,
            'non_governmental_organizations': non_governmental_organizations,
            'community_collections': community_collections,
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
