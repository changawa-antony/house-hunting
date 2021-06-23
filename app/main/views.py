from . import main
from flask import render_template

@main.route('/login')

def index ():
      
  return render_template('auth/login.html')
