from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from accounts.models import User


class TestAccountsApi(APITestCase):
    def test_registration(self):
        url = reverse('user_registration')

        data = dict(
            username="test",
            password="test_password"
        )
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_login(self):
        url = reverse('user_login')

        data = dict(
            username="test",
            password="test_password"
        )

        User.objects.create_user(**data)

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
