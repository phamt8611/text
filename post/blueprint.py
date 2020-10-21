from flask import Blueprint, render_template, request, url_for, redirect

from flask_security import login_required

from models import *
from app import db


post = Blueprint('post',__name__,template_folder='templates')


@post.route('/write', methods=['GET','POST'])
@login_required
def novel_write():
    if request.method == 'POST':
        title = request.form.get('title')
        image = request.form.get('image')
        body = request.form.get('body')
        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print("Tao Truyen That Bai")
        return redirect(url_for('post.novel_detail',slug=post.slug))
    tags = Tag.query.all()
    return render_template('post/post_write.html', tags=tags)


@post.route('/')
def novels_list():
    posts = Post.query.all()
    return render_template('post/post.html',posts=posts)


@post.route('/<slug>')
def novel_detail(slug):
    post = Post.query.filter(Post.slug==slug).first()
    return render_template('post/post_detail.html',post=post)

@post.route('/tags/<slug>')
def novel_tags(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    return render_template('post/tag_detail.html', tag=tag)
