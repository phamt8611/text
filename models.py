from datetime import datetime
from app import db
from time import time
import re


from flask_security import UserMixin, RoleMixin

def slugify(s):
    patterr = r'[^\w+]'
    return re.sub(patterr, '-', s)


posts_tags= db.Table('posts_tags',
        db.Column('post_id', db.Integer,
            db.ForeignKey('post.ids')),
        db.Column('tags_id', db.Integer,
            db.ForeignKey('tag.ids')))

roles_users = db.Table('roles_users',
        db.Column('user_id',db.Integer,
            db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer,
            db.ForeignKey('role.id')))

novels_users = db.Table('novels_users',
        db.Column('user_id', db.Integer,
            db.ForeignKey('user.id')),
        db.Column('novel_id',db.Integer,
            db.ForeignKey('novel.ids')))


class Post(db.Model):
    ids = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140),unique=True)
    body = db.Column(db.Text)
    authur = db.Column(db.Text)
    created = db.Column(db.DateTime,default=datetime.now())
    tags = db.relationship('Tag', secondary=posts_tags, backref=db.backref('posts'), lazy='dynamic')
    image = db.Column(db.Text)
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()
        self.generate_image()
    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
        else:
            self.slug = str(int(time()))
    def generate_image(self):
        if self.image:
            self.image = str(self.image)
        else:
            self.image = str("https://images5.fanpop.com/image/photos/26000000/Touhou-Yuri-touhou-yuri-26052870-567-567.jpg")

    def __repr__(self):
        return f'<Post id: {self.ids}, title: {self.title}'

class Novel(db.Model):
    ids = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.Text)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140),unique=True)
    content = db.Column(db.Text)
    authur = db.relationship('User', secondary=novels_users, backref=db.backref('novels'), lazy='dynamic')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()
    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title) 
        else:
            self.slug = str(int(time()))


class Tag(db.Model):
    ids = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.slug = slugify(self.title)

    def __repr__(self):
        return f'Tag id: {self.ids}, title: {self.title}'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    img_thumbnail = db.Column(db.String(255))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,backref=db.backref('users'),lazy='dynamic')


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
