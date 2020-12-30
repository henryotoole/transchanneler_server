# transchanneler/extensions.py
# Josh Reed 2020
#
# A short class which has all extensions of this webserver within.

from henryotoole_utils.config import load_config
import os

from transchanneler import config_name

#flask configuration
# This allows us to access the static flask server config without having to be in a static context.
app_config = load_config(os.environ[config_name])

#flask-SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()