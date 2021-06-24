from flask.helpers import url_for
from . import main
from flask_login import login_user ,logout_user, login_required
from flask import render_template, flash, redirect, url_for
from ..main.forms import BookApp
from ..models import User, Appointment
from .. import db
import datetime


@main.route('/sell')
def sell():
      
      
  return render_template('sell.html')

@main.route('/gallery')
def gallery():
      
      
  return render_template('gallery.html')


@main.route('/<user_id>/appointment')#add /<user_id> once authentication hase been added
@login_required #add login required as well
def book_appointment(user_id):
  form = BookApp()
  user_select = User.query.filter_by(user_id = user_id).first()
  user_id = user_select.user_id

  if form.validate_on_submit():
    title = form.aptmnt_title.data
    content = form.aptmnt_content.data
    y,m,d = form.date.data.split('/')
    when = datetime.datetime(int(y), int(m), int(d))

    appointment = Appointment(appointment_title = title, appointment_content = content, appointment_date = when, user = user_id)

    db.session.add(appointment)
    db.session.commit()

    flash('Appointment Created successfully', 'success')

    return redirect(url_for('main.index'))


  
  return render_template('appointment.html', title = 'Book Appointment', form = form)
