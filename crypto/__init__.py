"""
Created October 29, 2021
@author: oconn
"""
from flask import Flask  # From module flask import class Flask
# from config import Config  # get our Configuration variables

# Construct an instance of Flask class for our webapp
app = Flask(__name__)

from crypto import routes
# work around for circular imports