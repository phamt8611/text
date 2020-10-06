from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Chào mừng bạn đến với YuriNovel 2020"
@app.route("/test")
def words():
    return "YuriNovel cung cấp tiểu thuyết bách hợp miễn phí"

if __name__=="__main__":
    app.run()
