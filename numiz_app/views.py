from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView

from numiz_app.forms import CategoryForm, IssuerForm, DesignerForm, SubjectForm, CoinForm, CurrencyForm
from numiz_app.models import Category, Issuer, Designer, Subject, Coin, Currency


class IndexView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'base.html', {'categories': categories})


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'categories.html', {'categories': categories})


class AddCategory(LoginRequiredMixin, View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('category_coins')
        return render(request, 'form.html', {'form': form})


class CategoryDetail(DetailView):
    model = Category
    template_name = 'category_detail.html'


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'form.html'
    success_url = reverse_lazy('category_coins')


class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'form.html'
    success_url = reverse_lazy('category_coins')


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


class IssuerDetail(DetailView):
    model = Issuer
    template_name = 'issuer_detail.html'


class IssuerUpdate(LoginRequiredMixin, UpdateView):
    model = Issuer
    form_class = IssuerForm
    template_name = 'form.html'
    success_url = reverse_lazy('issuer_detail')


class IssuerDelete(LoginRequiredMixin, DeleteView):
    model = Issuer
    template_name = 'form.html'
    success_url = reverse_lazy('issuers')


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
            messages.success(request, 'Success new designer is add')
            return redirect('add_designer')
        else:
            messages.error(request, 'Error')
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
            messages.success(request, 'Success new subject is add')
            return redirect('add_subject')
        else:
            messages.error(request, 'Error')
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
            messages.success(request, 'Success new currency is add')
            return redirect('add_currency')
        else:
            messages.error(request, 'Error')
        return render(request, 'form.html', {'form': form})


class CoinsView(ListView):
    model = Coin
    context_object_name = 'coins'
    paginate_by = 10
    template_name = 'coins.html'


class AddCoin(LoginRequiredMixin, CreateView):
    model = Coin
    form_class = CoinForm
    template_name = 'form.html'
    success_url = reverse_lazy('coins')


class CoinDetail(DetailView):
    model = Coin
    template_name = 'coin_detail.html'


class CoinUpdate(LoginRequiredMixin, UpdateView):
    model = Coin
    form_class = CoinForm
    template_name = 'form.html'
    success_url = reverse_lazy('coin_detail')


class CoinDelete(LoginRequiredMixin, DeleteView):
    model = Coin
    template_name = 'form.html'
    success_url = reverse_lazy('coins')
