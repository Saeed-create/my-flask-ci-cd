# test_app.py
import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_main_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, CI/CD World', response.data)

    def test_test_route(self):
        response = self.app.get('/test')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is a test route!', response.data)

if __name__ == '__main__':
    unittest.main()
