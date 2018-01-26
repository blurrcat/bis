from rest_framework.test import APIClient
import pytest


@pytest.fixture
def api_client():
    return APIClient(format='json')


@pytest.fixture
def harry(db, django_user_model):
    return django_user_model.objects.create_user(
        username='harry',
        password='harry4u',
        email='harry@test.com',
    )


@pytest.fixture
def harry_client(harry, api_client):
    api_client.force_authenticate(harry)
    return api_client
