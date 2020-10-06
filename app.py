from flask import Flask
app = Flask(__name__)

YuriNovel = "YuriNovel cung cấp tiểu thuyết bách hợp miễn phí, được tạo ra bởi Tadashi Ringo"

@app.route("/")
def hello():
    return YuriNovel



if __name__=="__main__":
    app.run()
