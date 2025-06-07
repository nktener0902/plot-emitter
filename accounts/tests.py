from django.test import TestCase
from django.urls import resolve, reverse

from .views import login


class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse("accounts:login")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve("/accounts/login/")
        self.assertEqual(view.func, login)
