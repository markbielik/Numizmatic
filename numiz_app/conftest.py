import pytest
from django.contrib.auth.models import User
from django.test import Client as WebClient

from numiz_app.models import Category, Issuer, Coin, Designer, Subject, Currency


@pytest.fixture
def client():
    client = WebClient()
    return client


@pytest.fixture
def user2():
    x = User(username='marek')
    x.set_password('Dupa.812')
    x.save()
    return x


@pytest.fixture
def categories():
    lst = []
    a = Category.objects.create(name='Example1',
                                description="Lorem ipsum")
    lst.append(a)
    a = Category.objects.create(name='Example2')
    lst.append(a)
    return lst


@pytest.fixture
def category():
    a = Category.objects.create(name='Lorem',
                                description='Text lorem ipsum')
    return a


@pytest.fixture
def issuers():
    lst = []
    a = Issuer.objects.create(name='Example1',
                              description="Lorem ipsum",
                              short_name="Ex1")
    lst.append(a)
    a = Issuer.objects.create(name='Example2',
                              short_name="Ex2")
    lst.append(a)
    a = Issuer.objects.create(name='Example3',
                              description='Pan tadeusz')
    lst.append(a)
    return lst


@pytest.fixture
def issuer():
    a = Issuer.objects.create(name='Ala',
                              description='Ma kota',
                              short_name="AM")
    return a


@pytest.fixture
def designer():
    a = Designer.objects.create(first_name='Bielik',
                                last_name='Orzeł')
    return a


@pytest.fixture
def subject():
    a = Subject.objects.create(name='Powieści',
                               description='Bajki świata')
    return a


@pytest.fixture
def currency():
    a = Currency.objects.create(value=10,
                                unit="PLN")
    return a


@pytest.fixture
def coins(user2, issuer, subject, category, currency, designer):
    lst = []
    a = Coin.objects.create(title="ExampleCoin1", category=category, issuer=issuer,
                            subject=subject, face_value=currency,
                            description="short notice", stamp='mirror',
                            attempt="exap", issue_date="2021-12-12",
                            circulation=100, dimension=10.2, scales=8.2,
                            remarks=":)", user=user2)
    a.designer.set([designer])
    lst.append(a)
    return lst


@pytest.fixture
def coin(user2, issuer, subject, category, currency, designer):
    a = Coin.objects.create(title="ExampleCoin2", category=category, issuer=issuer,
                            subject=subject, face_value=currency,
                            description="notice", stamp="mirror",
                            attempt="ex", issue_date="2021-12-12",
                            circulation=100, dimension=10.2, scales=8.2,
                            remarks="-", user=user2)
    a.designer.set([designer])
    return a
