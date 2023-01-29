from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.db.models import Sum, Count
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Donation, Institution
from .forms import UserRegisterForm, LoginForm


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
    template_name = "giveaway/login.html"

    def get(self, request):
        form = UserRegisterForm()
        ctx = {
            'login_form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
            else:
                return redirect(reverse('register')+'#register-form')
        return redirect('index')


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
            'user_register_form': form,
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
