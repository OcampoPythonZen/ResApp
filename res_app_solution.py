""" Solution Test for backend-Resuelve
Author : Edgar Ocampo
"""
import requests
from requests.exceptions import RequestException


def get_response_api(url='https://my-json-server.typicode.com/hectorip/prueba-ing-backend/db') -> list:
    """
    definition for get the response url
    :param url: url direction of the data, it can use to test the local api created or the url declared by Resuelve Test
    :return: data as a dict {} to expose
    """
    data = []
    try:
        response = requests.get(url=url)
        data = response.json()['ejemplo_1']
    except RequestException as e:
        raise SystemExit(e)
    return data


class solution(object):
    """
    Globals vars to define the goals of each level player.
    a = 5, b = 10, c = 15 and level cuau = 20 goals per month.
    """
    player_level = ['a', 'b', 'c', 'cuau']
    player_goals = [5, 10, 15, 20]
    scopes = list(zip(player_level, player_goals))

    def get_group_percentage(self, data=[]) -> list:
        """ Function to calculate the group percentage of the team.
        :return: the list [] of the total percentage group for the len of players
        """
        data = get_response_api()
        team_goals = 0
        minimum_goals_per_level = []
        for player in data:
            if player['nivel'] == self.scopes[0][0].capitalize():
                minimum_goals_per_level.append(int(self.scopes[0][1]))
            elif player['nivel'] == self.scopes[1][0].capitalize():
                minimum_goals_per_level.append(int(self.scopes[1][1]))
            elif player['nivel'] == self.scopes[2][0].capitalize():
                minimum_goals_per_level.append(int(self.scopes[2][1]))
            elif player['nivel'] == self.scopes[3][0].capitalize():
                minimum_goals_per_level.append(int(self.scopes[3][1]))
            team_goals += player['goles']
        try:
            operation = (team_goals / sum(minimum_goals_per_level)) * 100
        except ZeroDivisionError:
            print(
                f'you cannot make divisions by zero. <{team_goals}, {minimum_goals_per_level}>')
        return [operation] * len(data)

    def get_individual_percentage(self, data=[]) -> list:
        """ Function to calculate the individual percentage player.
        :return: the list [] of the individual percentage
        """
        data = get_response_api()
        individual_goals = []
        for player in data:
            if player['nivel'] == self.scopes[0][0].capitalize():
                individual_goals.append(
                    (player['goles'] / self.scopes[0][1]) * 100)
            elif player['nivel'] == self.scopes[1][0].capitalize():
                individual_goals.append(
                    (player['goles'] / self.scopes[1][1]) * 100)
            elif player['nivel'] == self.scopes[2][0].capitalize():
                individual_goals.append(
                    (player['goles'] / self.scopes[2][1]) * 100)
            elif player['nivel'] == self.scopes[3][0].capitalize():
                individual_goals.append(
                    (player['goles'] / self.scopes[3][1]) * 100)
        return individual_goals

    def get_bonus_per_player(self, data=[]) -> list:
        """ Function to get the individual bonus team.
        :return: the list [] of the bonus per player
        """
        data = get_response_api()
        team_bonus = []
        for player in data:
            team_bonus.append(player['bono'])
        return team_bonus

    def get_salary_per_player(self, data=[]) -> list:
        """ Function to get the individual salary team.
        :return: the list [] of the salary per player
        """
        data = get_response_api()
        team_salary = []
        for player in data:
            team_salary.append(player['sueldo'])
        return team_salary

    def get_percentage_average(self) -> list:
        """ Function to calculate the fifty percent of both [(group percentage + individual percentage) / 2]
        :return: the list [] of the total per player percentage average
        """
        try:
            operation = [(x / 2) + (y / 2) for x, y in zip(self.get_group_percentage(),
                                                           self.get_individual_percentage())]
            operation = [val / 100 for val in operation]
        except ZeroDivisionError:
            print(
                f'you cannot make divisions by zero. <{self.get_group_percentage()}, {self.get_individual_percentage}>')
        return operation

    def get_total_bonus(self) -> list:
        """
        Function to calculate the total bonus per player.
        :return: a list [] of the results of total bonus
        """
        operation = []
        try:
            operation = [
                (x * y) for x, y in zip(self.get_percentage_average(), self.get_bonus_per_player())]
        except ValueError:
            print(
                f'products with zero give a null result. <{self.get_percentage_average()}, {self.get_bonus_per_player()}>')
        return operation

    def get_complete_salary(self) -> list:
        """
        Getting complete salary the bonus per player plus the monthly salary.
        :return: the list [] of the total per player
        """
        operation = []
        operation = [(x + y) for x, y in zip(self.get_total_bonus(),
                                             self.get_salary_per_player())]
        operation = [round(r, 2) for r in operation]
        return operation

    def filling_results(self, data=[]) -> list:
        """
        Filling the results per player into the API
        :return: a list [] of the results
        """
        data = get_response_api()
        for count, player in enumerate(data):
            player['sueldo_completo'] = self.get_complete_salary()[count]
        return data
