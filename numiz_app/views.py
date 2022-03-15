from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView

from numiz_app.forms import CategoryForm, IssuerForm, DesignerForm, SubjectForm, CoinForm, CurrencyForm
from numiz_app.models import Category, Issuer, Designer, Subject, Coin, Currency


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'categories.html', {'categories': categories})


class AddCategory(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('add_category')
        return render(request, 'form.html', {'form': form})


class IssuersView(View):
    def get(self, request):
        issuers = Issuer.objects.all()
        return render(request, 'issuers.html', {'issuers': issuers})


class AddIssuer(LoginRequiredMixin, View):

    def get(self, request):
        form = IssuerForm()
        issuers = Issuer.objects.all()
        return render(request, 'form.html', {'form': form,
                                             'issuers': issuers})

    def post(self, request):
        form = IssuerForm(request.POST)
        if form.is_valid():
            Issuer.objects.create(**form.cleaned_data)
            return redirect('issuers')
        return render(request, 'form.html', {'form': form})


class AddDesigner(LoginRequiredMixin, View):

    def get(self, request):
        form = DesignerForm()
        designers = Designer.objects.all()
        return render(request, 'form.html', {'form': form,
                                             'designers': designers})

    def post(self, request):
        form = DesignerForm(request.POST)
        if form.is_valid():
            Designer.objects.create(**form.cleaned_data)
            return redirect('add_designer')
        return render(request, 'form.html', {'form': form})


class AddSubject(LoginRequiredMixin, View):

    def get(self, request):
        form = SubjectForm()
        subjects = Subject.objects.all()
        return render(request, 'form.html', {'form': form,
                                             'subjects': subjects})

    def post(self, request):
        form = SubjectForm(request.POST)
        if form.is_valid():
            Subject.objects.create(**form.cleaned_data)
            return redirect('add_subject')
        return render(request, 'form.html', {'form': form})


class AddCurrency(LoginRequiredMixin, View):

    def get(self, request):
        form = CurrencyForm()
        currency = Currency.objects.all()
        return render(request, 'form.html', {'form': form,
                                             'subjects': currency})

    def post(self, request):
        form = CurrencyForm(request.POST)
        if form.is_valid():
            Currency.objects.create(**form.cleaned_data)
            return redirect('add_currency')
        return render(request, 'form.html', {'form': form})


class ListCoinsView(View):
    def get(self, request):
        coins = Coin.objects.all()
        return render(request, 'coins.html', {'coins': coins})


class AddCoin(View):
    def get(self, request):
        form = CoinForm()
        coins = Coin.objects.all()
        return render(request, 'form.html', {'form': form,
                                             'coins': coins})

    def post(self, request):
        form = CoinForm(request.POST)
        if form.is_valid():
            Coin.objects.create(**form.cleaned_data)
            return redirect('add_coin')
        return render(request, 'form.html', {'form': form})


class CoinView(CreateView):
    model = Coin
    form_class = CoinForm
    template_name = 'form.html'
    success_url = reverse_lazy('coins')


class CoinDetail(DetailView):
    model = Coin
    template_name = 'coin_detail.html'
