from django.shortcuts import render
from django.views import View

class LandingPage(View):
    def get(self, request):
        return render(request, "giveaway/index.html")


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