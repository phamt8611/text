from app import app
from flask import render_template

from models import *


#Trang Chủ
@app.route('/')
def index():
    novels = Novel.query.all()
    return render_template('index.html',novels=novels)

#hostname/<slug>
@app.route('/<slug>')
def novel_info(slug):
    novel = Novel.query.filter(Novel.slug==slug).first()
    return render_template('novel/info_novel.html', novel=novel)

