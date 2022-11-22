from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse


# Create your tests here.
class ViewTestCase(TestCase):
    """Тест представления с отправкой запроса в приложение."""

    def test_view_positive(self):
        """Выяснение url для запроса и совершение запроса."""
        url = reverse("increment")
        response = self.client.post(url)
        response = self.client.post(url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(3, response.json()["count"])
        print(response.content)
