from django.urls import reverse

from rest_framework import status

from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

from blog.models import Post

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        cls.post = Post.objects.create(
            title="Django for APIs",
            body="Nice body content",
            author= cls.user,
                
        )
    def test_api_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        self.assertContains(response, self.post)

# Create your tests here.
