from flask import Flask
from flask.templating import render_template
from . import main

@main.route('/')
def index():
    render_template('index.html')