"""
Unit test module for the following modules:
application.py, adt.py, arrays.py
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

    # Check for right content type
    def test_content_type(self):
        content_index = self.tester.get('/').content_type
        self.assertEqual(content_index, 'text/html; charset=utf-8')

    # Check for data returned
    def test_data(self):
        data = self.tester.get('/').data
        self.assertTrue(b'<a class="active" href="#home">Home</a>' in data)

class TestAdt(TestCase):
    def setUp(self):
        self.recommendation = adt.RecomendationADT('mirage', 'CT')
        self.player_stats = adt.PlayerStats('https://steamcommunity.com/profiles/76561198151223169/')

    def test_nickname(self):
        self.assertEqual(self.player_stats.soup_get_nickname(), 'Saitama')

    def test_kd(self):
        self.assertEqual(self.player_stats.steam_get_kd(), 0.75)

    def test_recommendation(self):
        self.recommendation.data[7] = 15000
        self.assertEqual(self.recommendation.advice(), "Enemy team has some money, approximately 3000 per head, so brobably they will make force-buy round, but there is a chance of semi-full-buy round. High chance of force-buy round, low chance of semi-buy round. They can push some spots, like middle or underpass, so be carefull and play slowly.")


class TestArrays(TestCase):
    def setUp(self):
        self.arrayD = arrays.Array(10)
        self.arrayD[0] = 2
        self.arrayD[4] = 7

    def test_set_items(self):
        self.assertEqual(self.arrayD[0], 2)
        self.assertEqual(self.arrayD[4], 7)
        self.assertEqual(self.arrayD[8], None)

    def test_len(self):
        self.assertEqual(len(self.arrayD), 10)

    def test_str(self):
        self.assertEqual(str(self.arrayD), '[2, None, None, None, 7, None, None, None, None, None]')


if __name__ == '__main__':
    main()