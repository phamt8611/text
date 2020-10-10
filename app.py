from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)



app.config.from_object(Config)

db = SQLAlchemy(app)
