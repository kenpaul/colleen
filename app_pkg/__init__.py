# This file get called during an import and initializes what symbols
# are exposed. It pulls in the classes Flask and Config from other python packages

from flask import Flask
from config import Config

# Now lets create an application object called "app" as an instance of class Flask
# remember thgat this will be exposed when we "import" this package so that other can
# reference app

app = Flask(__name__)
app.config.from_object(Config)

# the app_pkg package is the directroy containing routes so we can import
# that. This is down down here, as opposed to top, to work around
# "circular imports"

from app_pkg import routes

# to see what happned above check out the routes.py code. This essentailly
# kicks off the route code to listen for and process requests
