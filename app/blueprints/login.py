import os
from flask import (
  Blueprint, request, current_app, render_template
)
login_blueprint = Blueprint('login', __name__, template_folder='templates')

@login_blueprint.route('/')
def index():
   return render_template('index.html')

# login route
@login_blueprint.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
      error = 'Invalid Credentials. Please try again.'
    else:
      return redirect(url_for('index'))
  return render_template('login.html', error=error)
