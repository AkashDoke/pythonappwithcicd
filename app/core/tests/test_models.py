import email
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    #test creating new user with email
    def test_create_user_with_email_succeessful(self):
        email="info@arieotech.com"
        password="test123"
        user=get_user_model().objects.create_user(
            username=email,
            password=password
        )
        self.assertEqual(user.username,email)
        self.assertTrue(user.check_password(password))
        