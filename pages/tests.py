from urllib import response
from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, AboutPageView

# Create your tests here.

class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
    
    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_does_not_contain_incorect_html(self):
        self.assertNotContains(self.response, 'Ups, something goes wrong.')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')

    def test_homepage_resolver_url_homepageview(self):
        view = resolve('/')
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )

class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Ups, something goes wronge')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About This Page')
        
    def test_aboutpage_url_resolve_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__
        )
