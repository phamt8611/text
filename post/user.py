from flask import Blueprint




#Khai báo Blueprint
auth = Blueprint('auth',__name__)

#hostname/novel
@auth.route('/')
def auth():
    return "Admin"
