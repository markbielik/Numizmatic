from django import forms
from django.core.exceptions import ValidationError

from numiz_app.models import Category, Issuer, Subject, Designer, Coin, Currency


def check_negative_values(value):
    if value < 0.1:
        raise ValidationError("Incorrect, negative values")


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
        fields = ['name', 'description']


class CurrencyForm(forms.ModelForm):
    value = forms.IntegerField(validators=[check_negative_values])

    class Meta:
        model = Currency
        fields = '__all__'


class DesignerForm(forms.ModelForm):
    class Meta:
        model = Designer
        fields = ['first_name', 'last_name']


class CoinForm(forms.ModelForm):
    circulation = forms.IntegerField(validators=[check_negative_values])
    dimension = forms.DecimalField(validators=[check_negative_values])
    scales = forms.DecimalField(validators=[check_negative_values])

    class Meta:
        model = Coin
        exclude = ['slug', 'created', 'updated']
        widgets = {
            'designer': forms.CheckboxSelectMultiple,
            'description': forms.Textarea(attrs={'size': 1000}),
        }
