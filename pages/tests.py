from django.test import TestCase

# Create your tests here.
class TestPages(TestCase):
    def test_add_status_code(self):
        response =self.client.get('/')
        self.assertEqual(response.status_code,200)
