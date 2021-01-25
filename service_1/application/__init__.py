from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
app = Flask(__name__)
# initialising the app and setting the database uri 
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
db = SQLAlchemy(app)

from application import routes