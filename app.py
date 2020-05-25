''' We will create the api to use locally and test the url provided by github repository.
Author : Edgar Ocampo
'''
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
