from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Chào mừng bạn đến với YuriNovel 1"
@app.route("/test")

if __name__=="__main__":
    app.run()
