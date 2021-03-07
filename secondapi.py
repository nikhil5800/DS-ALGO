from flask import Flask
from flask_restful import Resource, Api, reqparse
from apprun import app

@app.route('/greet2')
def say_helol0():
    return 'helloooo22'

@app.route('/')
def sayyes():
    return 'yes running'

def run1():
    app.run(port=5001,debug=True)