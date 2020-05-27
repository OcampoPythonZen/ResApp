""" We will create the api to use locally and test the url provided by github repository.
Author : Edgar Ocampo
"""
import logging

from flask import Flask, jsonify, render_template
from db import RESUELVE_FC
from res_app_solution import solution

app = Flask(__name__)


@app.route('/')
def welcome_home() -> object:
    return render_template('welcome.html', title='RESUELVE')


@app.route('/resuelve_fc')
def get_players() -> dict:
    return jsonify(RESUELVE_FC)


@app.route('/team_salary_total')
def get_team_salary_total() -> dict:
    obj_solution = solution()
    logging.basicConfig(filename='resuelve.log',
                        format='%(asctime)s %(message)s', filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info('Starting with the calculations per player.')
    logger.info('Getting bonus per player')
    logger.info(obj_solution.get_bonus_per_player())
    logger.info('Getting salarys per player')
    logger.info(obj_solution.get_salary_per_player())
    logger.info('Getting average per player')
    logger.info(obj_solution.get_percentage_average())
    logger.info('Getting bonus per player')
    logger.info(obj_solution.get_total_bonus())
    logger.info('Getting total salarys per player and adding them.')
    logger.info(obj_solution.get_complete_salary())
    return jsonify(obj_solution.filling_results())


if __name__ == '__main__':
    app.run()
