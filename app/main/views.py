from . import main
from flask import render_template, flash, redirect, url_for
from flask_login import login_required
from ..main.forms import BookApp
from ..models import User, Appointment

@main.route('/')
def index ():
      
  return render_template('index.html')

