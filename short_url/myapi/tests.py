from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Token


from rest_framework import status
from rest_framework.test import APITestCase
from .models import Token

class TokenModelTests(APITestCase):

    url = '/api/token/'
    full_url = 'http://example.com/'
    short_url = 'aAb123'

    def test_create_model_object(self):
        Token.objects.create(
            full_url=self.full_url,
            short_url=self.short_url
        )

    def test_create_token_with_short_url(self):
        full_url = self.full_url
        short_url = self.short_url
        data = {'full_url': full_url, 'short_url': short_url}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Token.objects.count(), 1)
        token = Token.objects.get()
        self.assertEqual(token.full_url, full_url)
        self.assertEqual(token.short_url, short_url)

    def test_create_token_without_short_url(self):
        full_url = self.full_url
        data = {'full_url': full_url}
        response = self.client.post(self.url, data)
        # print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Token.objects.count(), 1)
        token = Token.objects.get()
        self.assertEqual(token.full_url, full_url)
        self.assertEqual(token.short_url, token.short_url)
        self.assertEqual(
            response.json()['full_url'],
            'http://example.com/',
            msg='Ошибка full_url'
        )

    def test_create_wrong_token(self):
        full_url = 'shasfd'
        data = {'full_url': full_url}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 400)

    def test_redirection(self):
        reponse = 


    