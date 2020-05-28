""" Test for app.py
Author: Edgar Ocampo
"""
import unittest
from app import app

class test_app(unittest.TestCase):

    def setUp(self) -> None:
        app.config['testing'] = True
        app.config['debug'] = False
        self.app = app.test_client()

    def test_welcome_home(self):
        response = self.app.get('/', follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def test_get_players(self):
        response = self.app.get('/resuelve_fc', follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def test_get_team_salary_total(self):
        response = self.app.get('/team_salary_total', follow_redirects=False)
        self.assertEqual(response.status_code, 200)

    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main()