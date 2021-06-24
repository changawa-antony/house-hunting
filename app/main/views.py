from flask.helpers import url_for
from . import main
from flask import render_template

@main.route('/')
def index():
      
      
  return render_template('index.html')

@main.route('/appointment')
def appointment():
      
      
  return render_template('appointment.html')

@main.route('/sell')
def sell():
      
      
  return render_template('sell.html')

@main.route('/gallery')
def gallery():
      
      
  return render_template('gallery.html')
