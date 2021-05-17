"""
Unit test module for the following modules:
application.py, adt.py, get_stats_module.py, arrays.py
for CS Rival Scanner.
"""
from unittest import TestCase, main
import application
import adt
import arrays
import get_stats_module

class TestApplication(TestCase):
    def setUp(self):
        self.tester = application.app.test_client(self)

    # Check for response
    def test_index(self):
        statuscode = self.tester.get('/').status_code
        self.assertEqual(statuscode, 200)

    def test_handle_player_info(self):
        statuscode = self.tester.post('/player_info').status_code
        self.assertEqual(statuscode, 200)

    def test_handle_recommendation(self):
        statuscode = self.tester.post('/recommendation').status_code
        self.assertEqual(statuscode, 200)

    # Check for right content type
    def test_content_type(self):
        content_index = self.tester.get('/').content_type
        content_player_info = self.tester.post('/player_info').content_type
        content_recommendation = self.tester.post('/recommendation').content_type
        self.assertEqual(content_index, 'text/html')
        self.assertEqual(content_player_info, 'text/html')
        self.assertEqual(content_recommendation, 'text/html')

    # Check for data returned
    def test_data(self):
        data = self.tester.get('/').data
        self.assertTrue(b'<a class="active" href="#home">Home</a>' in data)

class TestAdt(TestCase):
    pass


class TestArrays(TestCase):
    pass


class TestGetStats(TestCase):
    pass


if __name__ == '__main__':
    main()