from app import app
from app import db
import views

from post.blueprint import post


app.register_blueprint(post,url_prefix='/novel')



if __name__=='__main__':
    app.run()
