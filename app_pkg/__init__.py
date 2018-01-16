from flask import Flask
from config import Config

# create an application object as an instance of class Flask

app = Flask(__name__)
app.config.from_object(Config)

# the app_pkg package is the directroy containing routes.

from app_pkg import routes
