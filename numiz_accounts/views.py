from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic

from numiz_accounts.forms import LoginForm, UserBasicDataChangeForm, UserPasswordChangeForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is not None:
                login(request, user)
        return redirect('index')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "form.html"


class UserSettings(View):
    def get(self, request):
        basic_data = UserBasicDataChangeForm(prefix='basic_data_change_form',
                                             instance=request.user)
        return render(request, 'settings.html', {'basic_data': basic_data})


class ChangeBasicDataUser(View):
    def get(self, request):
        form = UserBasicDataChangeForm(prefix='basic_data_change_form',
                                       instance=request.user)
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = UserBasicDataChangeForm(data=request.POST,
                                       prefix='basic_data_change_form',
                                       instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('settings')
        return render(request, 'form.html', {'form': form})


class ChangeUserPassword(View):
    def get(self, request):
        form = UserPasswordChangeForm(prefix='password_change_form')
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = UserPasswordChangeForm(data=request.POST,
                                      prefix='password_change_form')
        if form.is_valid():
            cleaned = form.cleaned_data

            old_password = cleaned['old_password']
            password1 = cleaned['new_password1']
            password2 = cleaned['new_password2']

            if password1 == password2 and check_password(password=old_password,
                                                         encoded=request.user.password,
                                                         setter=make_password(password=old_password,
                                                                              salt=None,
                                                                              hasher='default')):
                user = request.user
                user.password = make_password(password=password1,
                                              salt=None,
                                              hasher='default')
                user.save()
                update_session_auth_hash(request, user)
            return redirect('settings')
        return render(request, 'form.html', {'form': form})

