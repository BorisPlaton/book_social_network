from django import forms
from django.contrib.auth import get_user_model

from account.models import Profile


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'email', 'password', 'password2')

    def clean_password2(self):
        if self.cleaned_data['password2'] != self.cleaned_data['password']:
            raise forms.ValidationError("Passwords doesn't match")
        return self.cleaned_data['password']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
