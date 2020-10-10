from flask import Blueprint, render_template

from models import Post


post = Blueprint('post',__name__,template_folder='templates')

@post.route('/')
def novels_list():
    posts = Post.query.all()
    return render_template('post/post.html',posts=posts)

@post.route('/<slug>')
def novel_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    return render_template('post/post_detail.html',post=post)
