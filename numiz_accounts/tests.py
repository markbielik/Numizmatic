import pytest
from django.test import TestCase
from django.urls import reverse


@pytest.mark.django_db
def test_login(client, user):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    dct = {
        'username': 'marek',
        'password': 'Dupa.812',
    }
    response = client.post(url, dct)
    assert response.status_code == 302
    assert response.wsgi_request.user.is_authenticated


def test_logout(client):
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302


def test_sing_up(client):
    url = reverse('sing_up')
    response = client.get(url)
    assert response.status_code == 200


def test_settings(client, user, user_settings):
    url = reverse('settings')
    response = client.get(url)
    assert response.status_code == 200
    dct = {
        'username': 'marek',
        'first_name': 'marek',
        'last_name': "bielik",
        'email': 'marek@example.pl',
    }
    response = client.post(url, dct)
    assert response.status_code == 302


def test_change_password(client):
    url = reverse('change_password')
    response = client.get(url)
    assert response.status_code == 200
    dct = {
        'old_password': 'Dupa.812',
        'new_password1': '812.dupA',
        'new_password2': "812.dupA",
    }
    response = client.post(url, dct)
    assert response.status_code == 200


def test_change_data(client, user_settings):
    url = reverse('change_data')
    response = client.get(url)
    assert response.status_code == 200
    dct = {
        'username': 'marek',
        'first_name': 'kubuś',
        'last_name': "puchatek",
        'email': 'marek@example.pl',
    }
    response = client.post(url, dct)
    assert response.status_code == 302

