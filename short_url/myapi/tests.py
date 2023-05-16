from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Token


from rest_framework import status
from rest_framework.test import APITestCase
from .models import Token

class TokenModelTests(APITestCase):

    url = '/api/token/'
    full_url = 'http://example.com/'

    def test_create_token_with_short_url(self):
        full_url = self.full_url
        short_url = 'abc123'
        data = {'full_url': full_url, 'short_url': short_url}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Token.objects.count(), 1)
        token = Token.objects.get()
        self.assertEqual(token.full_url, full_url)
        self.assertEqual(token.short_url, short_url)