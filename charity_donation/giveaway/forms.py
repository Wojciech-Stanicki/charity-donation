from django import forms

class UserRegisterForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password_repeat = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))


class UserUpdateForm(forms.Form):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput)
    last_name = forms.CharField(max_length=100, widget=forms.TextInput)
    email = forms.EmailField(max_length=100, widget=forms.EmailInput)
