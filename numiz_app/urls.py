"""numizmatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from numiz_app import views

urlpatterns = [
    path('category/', views.CategoryView.as_view(), name='category_coins'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('category_update/<int:pk>/', views.CategoryUpdate.as_view(), name='category_update'),
    path('category_del/<int:pk>/', views.CategoryDelete.as_view(), name='category_del'),
    path('add_category/', views.AddCategory.as_view(), name='add_category'),
    path('issuers/', views.IssuersView.as_view(), name='issuers'),
    path('issuer/<int:pk>', views.IssuerDetail.as_view(), name='issuer_detail'),
    path('issuer_update/<int:pk>/', views.IssuerUpdate.as_view(), name='issuer_update'),
    path('issuer_del/<int:pk>/', views.IssuerDelete.as_view(), name='issuer_del'),
    path('add_issuer/', views.AddIssuer.as_view(), name='add_issuer'),
    path('add_designer/', views.AddDesigner.as_view(), name='add_designer'),
    path('add_subject/', views.AddSubject.as_view(), name='add_subject'),
    path('add_currency/', views.AddCurrency.as_view(), name='add_currency'),
    path('list_coins/', views.CoinsView.as_view(), name='coins'),
    path('add_coin/', views.AddCoin.as_view(), name='add_coin'),
    path('add_coin2/', views.AddCoin2.as_view(), name='add_coin2'),
    path('coin/<int:pk>/', views.CoinDetail.as_view(), name='coin_detail'),
    path('coin_update/<int:pk>/', views.CoinUpdate.as_view(), name='coin_update'),
    path('coin_del/<int:pk>/', views.CoinDelete.as_view(), name='coin_del'),
]
