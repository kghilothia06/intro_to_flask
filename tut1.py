# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 18:47:00 2020

@author: KUSH
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world!"

@app.route("/kush")
def hello1():
    return "hello kush bro!"

app.run(debug=False)