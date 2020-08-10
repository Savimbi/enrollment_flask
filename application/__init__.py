

from config import Config
from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

from application import routes