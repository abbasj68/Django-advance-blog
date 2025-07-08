from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User
import pytest
from datetime import datetime
from rest_framework.authtoken.models import Token
from blog.models import Category


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(email="abbas@gmail.com", password="a/1234567")
    return user


@pytest.fixture
def test_category():
    return Category.objects.create(name="test-category")


@pytest.mark.django_db
class TestPostApi:
    # def setup_method(self):
    #     self.client = APIClient()
    #     self.user = User.objects.create_user(email='abbasj.gg@gmail.com', password='a/1234567')
    #     token = Token.objects.create(user=self.user)
    #     self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_post_response_200_status(self, api_client, common_user):
        api_client.force_login(user=common_user)
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201_status(
        self, api_client, common_user, test_category
    ):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
            "category": test_category,
        }
        api_client.force_login(user=common_user)
        # api_client.force_authenticate(user=common_user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_date_response_400_status(
        self, api_client, common_user
    ):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
        }
        api_client.force_login(user=common_user)
        # api_client.force_authenticate(user=common_user)
        response = api_client.post(url, data)

        assert response.status_code == 200
