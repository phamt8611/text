from app import app
from flask import render_template

from models import *


#Trang Chủ
@app.route('/')
def index():
    novels = Novel.query.all()
    return render_template('index.html',novels=novels)

