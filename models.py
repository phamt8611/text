from datetime import datetime
from app import db
from time import time
import re


def slugify(s):
    patterr = r'[^\w+]'
    return re.sub(patterr, '-', s)


class Post(db.Model):
    ids = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140),unique=True)
    body = db.Column(db.Text)
    authur = db.Column(db.Text)
    created = db.Column(db.DateTime,default=datetime.now())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()
        self.generate_authur()
    
    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
        else:
            self.slug = str(int(time()))
    def generate_authur(self):
        if self.authur:
            self.authur = str(self.authur)
        else:
            self.authur = str('Tasashi Ringo')

    def __repr__(self):
        return f'<Post id: {self.ids}, title: {self.title}'
