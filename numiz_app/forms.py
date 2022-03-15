from django import forms

from numiz_app.models import Category, Issuer, Subject, Designer, Coin, Currency


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class IssuerForm(forms.ModelForm):
    class Meta:
        model = Issuer
        fields = '__all__'


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'


class DesignerForm(forms.ModelForm):
    class Meta:
        model = Designer
        fields = '__all__'


class CoinForm(forms.ModelForm):
    class Meta:
        model = Coin
        fields = '__all__'

