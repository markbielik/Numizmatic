from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from numiz_app.forms import CategoryForm, IssuerForm, DesignerForm, SubjectForm
from numiz_app.models import Category, Issuer, Designer, Subject


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


class ListCoinsView(View):
    pass


class AddCoin(View):
    pass


class CoinDetailView(View):
    pass