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
    path('add_category/', views.AddCategory.as_view(), name='add_category'),
    path('issuers/', views.IssuersView.as_view(), name='issuers'),
    path('add_issuer/', views.AddIssuer.as_view(), name='add_issuer'),
    path('add_designer/', views.AddDesigner.as_view(), name='add_designer'),
    path('add_subject/', views.AddSubject.as_view(), name='add_subject'),
    path('list_coins/', views.ListCoinsView.as_view(), name='list_coins'),
    path('add_coin/', views.AddCoin.as_view(), name='add_coin'),
    path('coin/<int:pk>/', views.CoinDetailView.as_view(), name='coin_detail'),
]
