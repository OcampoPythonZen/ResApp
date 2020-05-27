""" Test for test_res_app_solution.py
Author: Edgar Ocampo
"""
import unittest
from res_app_solution import solution, get_response_api
from fake_db import FAKE_RESUELVE_FC


class test_res_app_solution(unittest.TestCase):

    def setUp(self) -> None:
        """
        set up of the unit test.
        :return: None values just define own global vars.
        """
        self.url = "https://my-json-server.typicode.com/hectorip/prueba-ing-backend/db"
        self.fake_url = "https://my-fake/url"
        self.instance = solution()
        self.fake_data = FAKE_RESUELVE_FC

    def test_get_response_api(self, url=''):
        """
        Test the response api, passing an url.
        RAISE SystemExit TEST whe pass a self.fake_url, but the system rise
        an error on it.
        """
        with self.assertRaises(SystemExit):
            api = get_response_api(self.url)
            self.assertIsInstance(api, list)

            fake_api = get_response_api(self.fake_url)
            self.assertIsInstance(fake_api, list)

    def test_get_group_percentage(self, data=[]):
        """
        Test the percentage of the team.
        """
        function = self.instance.get_group_percentage(get_response_api(self.url))
        self.assertIsInstance(function, list)

    def test_get_individual_percentage(self, data=[]):
        """
        Test the individual percentage per player.
        """
        function = self.instance.get_individual_percentage(get_response_api(self.url))
        self.assertIsInstance(function, list)

    def test_get_bonus_per_player(self, data=[]):
        """
        Test the bonus per player.
        """
        function = self.instance.get_bonus_per_player(get_response_api(self.url))
        self.assertIsInstance(function, list)

    def test_get_salary_per_player(self, data=[]):
        """
        Test the salary per player.
        """
        function = self.instance.get_salary_per_player(get_response_api(self.url))
        self.assertIsInstance(function, list)

    def test_get_percentage_average(self):
        """
        Test the percentage average.
        """
        function = self.instance.get_percentage_average()
        self.assertIsInstance(function, list)


    def test_get_total_bonus(self):
        """
        Test the total bonus per player.
        """
        function = self.instance.get_total_bonus()
        self.assertIsInstance(function, list)

    def test_get_complete_salary(self):
        """
        Test the complete salary per player.
        """
        function = self.instance.get_complete_salary()
        self.assertIsInstance(function, list)

    def test_filling_results(self, data=[]):
        """
        Test the filling of results on data given.
        """
        function = self.instance.filling_results(get_response_api(self.url))
        self.assertIsInstance(function, list)

    def tearDown(self) -> None:
        """
        tear down of the unit test.
        :return: None values just define down test.
        """
        pass

if __name__ == '__main__':
    unittest.main()
