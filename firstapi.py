from flask import Flask
from flask_restful import Resource, Api, reqparse
from apprun import app

@app.route('/greet')
def say_helolo():
    return 'helloooo'


def run2():
    app.run(port=5002,debug=True)