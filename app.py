""" We will create the api to use locally and test the url provided by github repository.
Author : Edgar Ocampo
"""
import logging
import os
from datetime import datetime
from uuid import uuid4

from flask import Flask, jsonify, render_template
from db import RESUELVE_FC

app = Flask(__name__)


@app.route('/')
def welcome_home() -> object:
    return render_template('welcome.html', title='RESUELVE')


@app.route('/resuelve_fc')
def get_players() -> dict:
    return jsonify(RESUELVE_FC)


if __name__ == '__main__':
    app.run()
