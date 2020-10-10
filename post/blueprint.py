from flask import Blueprint, render_template

post = Blueprint('post',__name__,template_folder='templates')

@post.route('/')
def novels_list():
    return render_template('post/post.html')
