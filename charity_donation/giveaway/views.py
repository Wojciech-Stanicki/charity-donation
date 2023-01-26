from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum, Count
from django.contrib.auth.models import User
from .models import Donation, Institution
from .forms import UserRegisterForm


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
    template_name = "giveaway/register.html"

    def get(self, request):
        form = UserRegisterForm()
        ctx = {
            'user_register_form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = UserRegisterForm(request.POST)
        ctx = {
            'user_register_form': form
        }
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data.get('email'),
                email=form.cleaned_data.get('email'),
                password=form.cleaned_data.get('password'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
            )
            return redirect("login")
        return render(request, self.template_name, ctx)


class FormConfimation(View):
    def get(self, request):
        return render(request, "giveaway/form-confirmation.html")
