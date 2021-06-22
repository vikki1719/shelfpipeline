from django.test import TestCase

# Create your tests here.
# django 2.x
from django.urls import reverse

class urlss(TestCase):
    def test_home(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
