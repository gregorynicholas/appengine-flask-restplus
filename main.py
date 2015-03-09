"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

# example of simple admin blueprint
from apps import admin
app = Flask(__name__)

# configure debugging
app.debug = True

# register blueprints
app.register_blueprint(admin.bp, url_prefix='/admin')

