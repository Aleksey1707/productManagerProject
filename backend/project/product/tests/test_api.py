from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from product.models import Category


# ToDo Написать тесты CRUD API для Product, Shop, ProductStat


class TestCategoryApi(APITestCase):
    def test_list_category(self):
        url = reverse('categories-list')

        c1 = Category.objects.create(name="к1")
        c1.children.create(name="к11")

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_category(self):
        url = reverse('categories-detail', kwargs=dict(pk=2))

        c1 = Category.objects.create(name="к1")
        c1.children.create(name="к11")

        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        url = reverse('categories-list')

        data = dict(
            name="к1"
        )
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
        url = reverse('categories-detail')

        Category.objects.create(name="к1")

        data = dict(
            name="к1"
        )
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

    def test_delete_category(self):
        url = reverse('categories-detail', kwargs=dict(pk=2))

        c1 = Category.objects.create(name="к1")
        c1.children.create(name="к11")

        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 1)

        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
