from flask import Flask, render_template, redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

#Admin, AdminIndexView
from flask_admin import Admin, AdminIndexView,expose
from flask_admin.contrib.sqla import ModelView

#Flask_mail
from flask_mail import Mail


from flask_security import SQLAlchemyUserDatastore, Security, current_user
from config import Config




#Khai báo về ứng dụng web
app = Flask(__name__)
#Khai báo Config trong config.py
app.config.from_object(Config)
#Khai báo Database SQLAlchemy
db = SQLAlchemy(app)


mail = Mail(app)



from models import *

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)







#Bảng Điều Khiển Admin
class AdminView(ModelView):
    def is_accessible(self):
        return current_user.has_role('admin')

class NormalView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    def not_auth(self):
        return "Vui lòng đăng nhập"

#Chạy Admin-Panel
#admin = Admin(app,'Admin',base_template='index.html', template_mode='admin')
admin = Admin(app, 'Admin',base_template='admin/base.html',template_mode='admin')

#Hiện và xem Database trong Admin-Panel
#Tag, User, Role
admin.add_view(AdminView(Novel, db.session))
admin.add_view(AdminView(Tag, db.session))
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Role, db.session))








#Flask Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
