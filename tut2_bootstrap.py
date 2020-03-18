# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:16:47 2020

@author: KUSH
"""

from flask import Flask , render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/about")
def hello1():
    name="kush"
    return render_template("about.html",name2=name)

@app.route("/bootstrap")
def bstrap():
    return render_template("bootstrap.html")
app.run(debug=False)
