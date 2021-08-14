"""
This file contains the tests for the views of the 'core' application.
"""

from django.test import TestCase
from .views import home, about

class TestVida(TestCase):
    """
    Class containing the tests for the 'core' application.
    """

    def setUp(self) -> None:
        """
        Set-up method that's run before all tests.
        """
        self.test_urls = {
            'home': '/',
            'about': '/about/'
        }
        self.test_redirect_urls = {
            'home': '',
            'about': '/about'
        }

    def test_home(self) -> None:
        """
        Tests the 'home' page.
        """
        # Ensure that the 'home' response matches the given function in views.py
        response = self.client.get(self.test_urls['home'])
        self.assertEqual(response.resolver_match.func, home)

    def test_about(self) -> None:
        """
        Tests the 'about' page.
        """
        # Ensure that the 'about' response matches the given function in views.py
        response = self.client.get(self.test_urls['about'])
        self.assertEqual(response.resolver_match.func, about)
