from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Chào mừng bạn đến với YuriNovel 2020"
def words():
    return "YuriNovel cung cấp tiểu thuyết bách hợp miễn phí"
