from app import app
from app import db
import views

from post.blueprint import post

#Đăng ký blueprint cho "post", url là "/novel"
app.register_blueprint(post,url_prefix='/novel')

#Chạy ứng dụng
if __name__=='__main__':
    app.run()
