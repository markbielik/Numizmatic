import pytest
from django.urls import reverse

from numiz_app.models import Category, Designer, Issuer, Subject, Currency, Coin


@pytest.mark.django_db
def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


# CATEGORY TEST
@pytest.mark.django_db
def test_categories(client, categories):
    url = reverse('category_coins')
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context['categories'].count() == len(categories)
    for item in categories:
        assert item in context['categories']


@pytest.mark.django_db
def test_category_add_view_without_login(client):
    url = reverse('add_category')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_category_add_view_with_login(user2, client):
    url = reverse('add_category')
    client.force_login(user2)
    dtc = {
        'name': 'Reksio',
        'description': "wow wow"
    }
    client.post(url, dtc)
    assert Category.objects.get(**dtc)


@pytest.mark.django_db
def test_category_detail(client, category):
    url = reverse('category_detail', args=(category.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_category_update_without_login(client, category):
    url = reverse('category_update', args=(category.id,))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_category_update_with_login(user2, client, category):
    client.force_login(user2)
    url = reverse('category_update', args=(category.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_category_delete_without_login(client, category):
    url = reverse('category_del', args=(category.id,))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_category_delete_with_login(user2, client, category):
    url = reverse('category_del', args=(category.id,))
    client.force_login(user2)
    response = client.get(url)
    assert response.status_code == 200


# ISSUERS TEST
@pytest.mark.django_db
def test_issuers(client, issuers):
    url = reverse('issuers')
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context['issuers'].count() == len(issuers)
    for item in issuers:
        assert item in context['issuers']


@pytest.mark.django_db
def test_issuer_add_view_without_login(client):
    url = reverse('add_issuer')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_issuer_add_view_with_login(user2, client):
    url = reverse('add_issuer')
    client.force_login(user2)
    dtc = {
        'name': 'Bank',
        'description': "Duży bank",
        'short_name': 'BD'
    }
    client.post(url, dtc)
    assert Issuer.objects.get(**dtc)


@pytest.mark.django_db
def test_issuer_detail(client, issuer):
    url = reverse('issuer_detail', args=(issuer.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_issuer_update_without_login(client, issuer):
    url = reverse('issuer_update', args=(issuer.id,))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_issuer_update_with_login(user2, client, issuer):
    client.force_login(user2)
    url = reverse('issuer_update', args=(issuer.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_issuer_delete_without_login(client, issuer):
    url = reverse('issuer_del', args=(issuer.id,))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_issuer_delete_with_login(user2, client, issuer):
    url = reverse('issuer_del', args=(issuer.id,))
    client.force_login(user2)
    response = client.get(url)
    assert response.status_code == 200


# COIN TEST
@pytest.mark.django_db
def test_coins(client, coins):
    url = reverse('coins')
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context['coins'].count() == len(coins)
    for item in coins:
        assert item in context['coins']


@pytest.mark.django_db
def test_coins_add_view_without_login(client):
    url = reverse('add_coin')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_coin_add_view_with_login(user2, client, category, designer, issuer, currency, subject):
    url = reverse('add_coin')
    client.force_login(user2)
    dtc = {
        'title': "ExampleCoin1",
        'designer': [designer.id],
        'category': str(category.id),
        'issuer': str(issuer.id),
        'subject': str(subject.id),
        'face_value': str(currency.id),
        'description': "short notice",
        'stamp': 'mirror',
        'attempt': "exap",
        'issue_date': "2021-12-12",
        'circulation': 100,
        'dimension': 10.2,
        'scales': 8.2,
        'remarks': "brak",
        'created': '2022-03-18',
        'updated': '2022-03-18',
        'slug': 'examplecoin1',
        'user': str(user2.id)
    }
    client.post(url, dtc)
    assert Coin.objects.get(title="ExampleCoin1")


@pytest.mark.django_db
def test_coin_detail(client, coin):
    url = reverse('coin_detail', args=(coin.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_coin_update_without_login(client, coin):
    url = reverse('coin_update', args=(coin.id,))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_coin_update_with_login(user2, client, coin):
    client.force_login(user2)
    url = reverse('coin_update', args=(coin.id,))
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_coin_delete_without_login(client, coin):
    url = reverse('coin_del', args=(coin.id,))
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_coin_delete_with_login(user2, client, coin):
    url = reverse('coin_del', args=(coin.id,))
    client.force_login(user2)
    response = client.get(url)
    assert response.status_code == 200


# DESIGNER TEST
@pytest.mark.django_db
def test_designer_add_view_without_login(client):
    url = reverse('add_designer')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_designer_add_view_with_login(user2, client):
    url = reverse('add_designer')
    client.force_login(user2)
    dtc = {
        'first_name': 'Jan',
        'last_name': "Sobieski"
    }
    client.post(url, dtc)
    assert Designer.objects.get(**dtc)


# SUBJECT TEST
@pytest.mark.django_db
def test_subject_add_view_without_login(client):
    url = reverse('add_subject')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_subject_add_view_with_login(user2, client):
    url = reverse('add_subject')
    client.force_login(user2)
    dtc = {
        'name': 'Ipsum',
        'description': "lorem ipsum"
    }
    client.post(url, dtc)
    assert Subject.objects.get(**dtc)


# CURRENCY TEST
@pytest.mark.django_db
def test_currency_add_view_without_login(client):
    url = reverse('add_currency')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_currency_add_view_with_login(user2, client):
    url = reverse('add_currency')
    client.force_login(user2)
    dtc = {
        'value': 10,
        'unit': 'euro'
    }
    client.post(url, dtc)
    assert Currency.objects.get(value=10)
