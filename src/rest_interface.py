"""This module contains REST interface logic"""
from flask import Flask

app = Flask(__name__)

@app.route('/accounts')
def get_accounts():
    
    return "Hello World"