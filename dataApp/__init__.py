#!/usr/bin/python3
from flask import Flask, render_template, g, request, url_for, redirect, session, flash
from toCSV import main as toCSV
from decoder import main as decoder
from plotTest import main as plotTest
import sys
import os

app = Flask(__name__)


@app.route('/',methods=["GET","POST"])
def homepage():
    if request.method == "POST":
        toCSV(request.form['data'])
        decoder()
        plotTest()
        return(redirect(url_for('static',filename='data.png')))
    return(render_template('home.html'))





if __name__=="__main__":
    app.run()
