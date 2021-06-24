from flask.helpers import url_for
from . import main
from flask import render_template
from flask_login import login_user ,logout_user, login_required

@main.route('/login')
@login_required
def login ():
  return render_template('login.index')

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
