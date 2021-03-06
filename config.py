import os

BASE_DIR = os.path.dirname(os.path.abspath(__name__))



class Config:

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR,'database.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Ringokey'
    SECURITY_PASSWORD_SALT = 'Ringopwsat'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True


    SECURITY_EMAIL_SUBJECT_PASSWORD_RESET = "Reset lại mật khẩu"


