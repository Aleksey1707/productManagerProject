from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from accounts.models import User
from product.models import Category


# ToDo Написать тесты CRUD API для Product, Shop, ProductStat


class TestCategoryApi(APITestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='tester',
                                            password='test_password')
        cls.token = Token.objects.create(user=cls.user)

    def _set_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def _remove_token(self):
        self.client.credentials()

    def test_list_category(self):
        url = reverse('categories-list')

        c1 = Category.objects.create(name="к1")
        c1.children.create(name="к11")

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_category(self):
        c1 = Category.objects.create(name="к1")
        c11 = c1.children.create(name="к11")

        url = reverse('categories-detail', kwargs=dict(pk=c11.pk))

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        url = reverse('categories-list')

        data = dict(
            name="к1"
        )

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Category.objects.count(), 0)

        self._set_token()
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        category = Category.objects.get()
        self.assertEqual(category.name, "к1")
        self.assertIsNone(category.parent)

        # =====

        data = dict(
            name="к11",
            parent=1
        )
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)
        category = Category.objects.last()
        self.assertEqual(category.name, "к11")
        self.assertEqual(category.parent_id, 1)

    def test_update_category(self):
        c1 = Category.objects.create(name="к1")

        url = reverse('categories-detail', kwargs=dict(pk=c1.pk))

        data = dict(
            name="к1е"
        )

        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Category.objects.count(), 1)
        c1.refresh_from_db()
        self.assertEqual(c1.name, "к1")
        self.assertIsNone(c1.parent)

        self._set_token()
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 1)
        c1.refresh_from_db()
        self.assertEqual(c1.name, "к1е")
        self.assertIsNone(c1.parent)

    def test_delete_category(self):
        c1 = Category.objects.create(name="к1")
        c11 = c1.children.create(name="к11")

        url = reverse('categories-detail', kwargs=dict(pk=c11.pk))

        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Category.objects.count(), 2)

        self._set_token()

        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 1)

        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def tearDown(self) -> None:
        Category.objects.all().delete()
