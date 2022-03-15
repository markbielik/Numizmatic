import pytest
from django.contrib.auth.models import User
from django.test import Client as WebClient


@pytest.fixture
def user():
    x = User(username='marek')
    x.set_password('Dupa.812')
    x.save()
    return x

@pytest.fixture
def user2():
    x = User(username='marek', password='Dupa.812')
    return x

@pytest.fixture
def user_settings():
    x = User(username='marek',
             first_name='marek',
             last_name="bielik",
             email='marek@example.pl')
    return x
