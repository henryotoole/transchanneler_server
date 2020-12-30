# provod_server/__init__.py
# Josh Reed 2020
#
# This is the main provod server module file. Importing it will start the flask server if this is the __main__
# thread.

# Define app-wide constants
config_name = 'FLASK_CONFIG_TRC'

# Imports from our modules
import transchanneler.extensions as ext

# Flask imports
import flask_sqlalchemy
from flask import Flask

#Sets up the extensions and other path-containing files in this module
def setup():
	#Configure this server instance (sets constant strings)
	app.config.from_envvar(config_name)
	register_extensions(app)
	#Import all path-containing files
	#import transchanneler.___

#We register extensions in this way to prevent circular import references. Simply provides a
#reference to 'app' to each extension.
def register_extensions(app):
	ext.db = flask_sqlalchemy.SQLAlchemy(app)


#This code is called whenever the module is imported, OR
#When gunicorn calls this in the command
app = Flask(__name__, static_url_path='') # The static url path is set here so we can serve static files for the dev server.
setup()