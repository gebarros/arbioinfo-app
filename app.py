# import the Flask class from the flask module
from flask import Flask, render_template

# Create the app object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def index():
   return render_template('index.html')


# Start the server with the 'run()' method
if __name__ == '__main__':
   app.run(debug = True)