from django.test import TestCase
from django.urls import reverse


class SnackTests(TestCase):

    def test_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_templates(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")

    # def test_templates_detail(self):
    #     url = reverse("snack_detail")
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, "snack_detail.html")
    #     self.assertTemplateUsed(response, "base.html")
