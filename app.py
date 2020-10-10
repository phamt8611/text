from flask import Flask, render_template
from config import Config
from post.blueprint import post

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(post,url_prefix='/novel')
