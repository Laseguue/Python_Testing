import unittest
from unittest.mock import patch
from server import create_app

class TestIntegrationServerMethods(unittest.TestCase):

    def setUp(self):
        self.app_instance = create_app()
        self.app_instance.config['TESTING'] = True
        self.app = self.app_instance.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the GUDLFT Registration Portal!', response.data)

    def test_points_display(self):
        response = self.app.get('/pointsDisplay')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Points available for each club', response.data)

if __name__ == '__main__':
    unittest.main()
