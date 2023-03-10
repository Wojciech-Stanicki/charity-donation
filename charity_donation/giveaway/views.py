from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.db.models import Sum, Count
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Donation, Institution, Category
from .forms import UserRegisterForm, LoginForm, UserUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


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


class AddDonation(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        categories = Category.objects.all()
        ctx = {
            'categories': categories,
        }
        return render(request, "giveaway/form.html", ctx)


class Login(View):
    template_name = "giveaway/login.html"

    def get(self, request):
        form = LoginForm()
        ctx = {
            'login_form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = LoginForm(request.POST)
        next_page = self.request.GET.get('next')
        if next_page == reverse('add-donation'):
            redirect_url = next_page + '#donation-form'
        else:
            redirect_url = reverse('index')
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user:
                login(request, user)
            else:
                return redirect(reverse('register') + '#register-form')
        return redirect(redirect_url)


class Logout(View):
    def get(self, request):
        logout(request)
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


class UserProfile(View):
    template_name = "giveaway/user-profile.html"

    def get(self, request):
        current_user = request.user
        user_donations = current_user.donation_set.all().order_by('is_taken', 'pick_up_date', 'pick_up_time')
        ctx = {
            'user_donations': user_donations,
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        current_user = request.user
        user_donations = current_user.donation_set.all()
        for donation in user_donations:
            checkbox_state = request.POST.get(str(donation.id))
            if checkbox_state is None:
                new_is_taken_value = False
            else:
                new_is_taken_value = True
            donation.is_taken = new_is_taken_value
            donation.save()
        user_donations = current_user.donation_set.all().order_by('is_taken', 'pick_up_date', 'pick_up_time')
        ctx = {
            'user_donations': user_donations,
        }
        return render(request, self.template_name, ctx)


class UpdateUserProfile(LoginRequiredMixin, View):
    login_url = 'login'
    template_name = "giveaway/user-profile-settings.html"

    def get(self, request):
        current_user = self.request.user
        form = UserUpdateForm(initial={'first_name': current_user.first_name,
                                       'last_name': current_user.last_name,
                                       'email': current_user.email,
                                       })
        ctx = {
            'user_profile_data_form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        current_user = self.request.user
        form = UserUpdateForm(request.POST)
        ctx = {
            'user_profile_data_form': form,
        }
        if form.is_valid():
            User.objects.filter(id=current_user.id).update(
                username=form.cleaned_data.get('email'),
                email=form.cleaned_data.get('email'),
                first_name=form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
            )
            return redirect("profile-settings")
        return render(request, self.template_name, ctx)


class FormConfimation(View):
    def get(self, request):
        return render(request, "giveaway/form-confirmation.html")
