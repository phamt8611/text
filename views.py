from app import app
from flask import render_template

from models import *


#Trang Chủ
@app.route('/')
def index():
    return render_template('index.html')

