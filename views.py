#!/usr/bin/python3
""" Routes to the App """

from flask import render_template, Flask
from models import app

@app.route('/')
@app.route('/home')
def home():
    """ Home Page """
    return render_template('index.html')

@app.route('/shop')
def shop():
    """ Market place """
    return render_template('shop.html')

