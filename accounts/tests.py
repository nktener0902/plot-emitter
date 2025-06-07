from django.test import TestCase
from django.urls import resolve, reverse

from .views import login


class SignUpTests(TestCase):
    def test_signup_status_code(self):
        url = reverse("login")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        view = resolve("/login/")
        self.assertEquals(view.func, login)
