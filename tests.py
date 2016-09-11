import unittest

from app import app
from config import TestingConfig


class TestCase(unittest.TestCase):
    def setUp(self):
        app.config.from_object(TestingConfig)
        self.app = app.test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(200, response.status_code)
        self.assertEqual('text/html; charset=utf-8', response.content_type)
        print(response.data)


if __name__ == '__main__':
    unittest.main()
