from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from expression.models import InputQuery

class IndexViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_get_index_authenticated(self):
        response = self.client.get(reverse('expression:index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('latest_query_list', response.context)

    def test_post_valid_expression(self):
        data = {
            'expression': 'x**2',
            'noise_function': 'none',
            'fineness': '1',
            'x_min_range': '0',
            'x_max_range': '2',
            'comment': 'test',
        }
        response = self.client.post(reverse('expression:index'), data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('plots', response.context)
        self.assertEqual(response.context['message'], '')
        self.assertEqual(InputQuery.objects.count(), 1)

    def test_post_invalid_expression(self):
        data = {
            'expression': '2x',  # invalid for eval
            'noise_function': 'none',
            'fineness': '1',
            'x_min_range': '0',
            'x_max_range': '2',
            'comment': 'test',
        }
        response = self.client.post(reverse('expression:index'), data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.context)
        self.assertIn('Invalid expressoin', response.context['message'])
        self.assertEqual(InputQuery.objects.count(), 0)

    def test_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse('expression:index'))
        self.assertNotEqual(response.status_code, 200)

    def post(self, path, data=None, content_type=None, follow=False, secure=False, **extra):
        # テスト時はrequestにtest_case属性を付与してlogging抑制
        extra['test_case'] = True
        return super().post(path, data=data, content_type=content_type, follow=follow, secure=secure, **extra)
