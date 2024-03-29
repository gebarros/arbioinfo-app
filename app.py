import os

from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.paht.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, database.db))

# Create the app object
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

# use decorators to link the function to a url
@app.route('/')
def index():
   return render_template('index.html')

# login route
@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != 'admin' or request.form['password'] != 'admin':
      error = 'Invalid Credentials. Please try again.'
    else:
      return redirect(url_for('index'))
  return render_template('login.html', error=error)


# Start the server with the 'run()' method
if __name__ == '__main__':
   app.run(debug = True)
