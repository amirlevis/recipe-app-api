# from django.db import models
from core import models
from django.test import TestCase
from django.contrib.auth import get_user_model


def sample_user(email='olegneduda@moshecohen.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        ''' Test Create a new user with an email is successful'''

        email = 'test@moshecohen.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
            )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized """
        email = 'test@MOSHECOHEN.com'
        user = get_user_model().objects.create_user(email, 'sdkjsdkj')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        ''' Test creating user with no email raises error '''

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'sdsdsds')

    def test_create_new_superuser(self):
        '''Test creating new super user'''

        user = get_user_model().objects.create_superuser(
            email='ksdfjdkf@moshecohen.com',
            password='sadsdfsdfds')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""

        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan',
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingrdient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucamber'
        )

        self.assertEqual(str(ingredient), ingredient.name)
