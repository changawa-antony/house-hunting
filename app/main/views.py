from . import main
from flask import render_template
from flask_login import login_user ,logout_user, login_required



@main.route('/login')
@login_required
def index ():
      
  return render_template('index.html')
