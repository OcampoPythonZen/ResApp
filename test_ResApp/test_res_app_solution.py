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
        self.fake_url = "https://myfake-url"
        self.fake_db = FAKE_RESUELVE_FC
        self.obj = solution()

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


    def test_get_group_percentage(self):
        """
        Test the percentage of the team.
        """
        with self.assertRaises(ZeroDivisionError):
            function = self.obj.get_group_percentage()
            self.assertIsInstance(function, list)

            function_fake = self.fake_db
            self.assertIsInstance(function_fake, list)


    def test_get_individual_percentage(self):
        """
        Test the individual percentage per player.
        """
        function = self.obj.get_individual_percentage()
        self.assertIsInstance(function, list)

    def test_get_bonus_per_player(self):
        """
        Test the bonus per player.
        """
        function = self.obj.get_bonus_per_player()
        self.assertIsInstance(function, list)

    def test_get_salary_per_player(self):
        """
        Test the salary per player.
        """
        function = self.obj.get_salary_per_player()
        self.assertIsInstance(function, list)

    def test_get_percentage_average(self):
        """
        Test the percentage average.
        """
        function = self.obj.get_percentage_average()
        self.assertIsInstance(function, list)


    def test_get_total_bonus(self):
        """
        Test the total bonus per player.
        """
        function = self.obj.get_total_bonus()
        self.assertIsInstance(function, list)

    def test_get_complete_salary(self):
        """
        Test the complete salary per player.
        """
        function = self.obj.get_complete_salary()
        self.assertIsInstance(function, list)

    def test_filling_results(self):
        """
        Test the filling of results on data given.
        """
        function = self.obj.filling_results()
        self.assertIsInstance(function, list)

    def tearDown(self) -> None:
        """
        tear down of the unit test.
        :return: None values just define down test.
        """
        pass

    if __name__ == '__main__':
        unittest.main()