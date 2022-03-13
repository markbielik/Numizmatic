from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms


def passwd_length_validation(value):
    if len(value) < 8:
        raise ValidationError("Password to short")


class LoginForm(forms.Form):
    username = forms.CharField(label='User')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}
    ))


class UserBasicDataChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'email']


class UserPasswordChangeForm(forms.Form):
    old_password = forms.CharField(label='Old password',
                                   min_length=8,
                                   widget=forms.PasswordInput,
                                   required=True)
    new_password1 = forms.CharField(label='New password',
                                    min_length=8,
                                    widget=forms.PasswordInput,
                                    required=True)
    new_password2 = forms.CharField(label='Repeat new password',
                                    min_length=8,
                                    widget=forms.PasswordInput,
                                    required=True)
