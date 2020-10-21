from flask import Flask, render_template, redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


from flask_security import SQLAlchemyUserDatastore, Security, current_user
from config import Config


app = Flask(__name__)


app.config.from_object(Config)

db = SQLAlchemy(app)


from models import *

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


#Bảng Điều Khiển Admin

class AdminView(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('seurity.login', next=request.url))

admin = Admin(app,'YuriNovel-Admin', template_mode='bootstrap3')

admin.add_view(AdminView(Tag, db.session))
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Role, db.session))

#Flask Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
