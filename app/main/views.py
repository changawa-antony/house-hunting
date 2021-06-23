from . import main
from flask import render_template, flash, redirect, url_for
from flask_login import login_required
from ..main.forms import BookApp
from ..models import User, Appointment

@main.route('/')
def index ():
      
  return render_template('index.html')

@main.route('/<user_id>/bookappointment')#add /<user_id> once authentication hase been added
# @login_required #add login required as well
def book_appointment(user_id):
  form = BookApp()
  user_select = User.query.filter_by(user_id = user_id).first()
  user_id = user_select.user_id

  if form.validate_on_submit():
    title = form.aptmnt_title.data
    content = form.aptmnt_content.data
    when = form.aptmnt_when.data

    appointment = Appointment(appointment_title = title, appointment_content = content, appointment_date = when, user = user_id)

    db.session.add(appointment)
    db.session.commit()

    flash('Appointment Created successfully', 'success')

    return redirect(url_for('main.index'))


  
  return render_template('bookappointment.html', title = 'Book Appointment')
