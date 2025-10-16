from django.test import TestCase
from django.urls import reverse

class CoreTemplatesViewTests(TestCase):
    def test_index_page_loads_successfully(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/index.html")
        self.assertContains(response, "Test content")
        
