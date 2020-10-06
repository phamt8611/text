from flask import Flask, render_template


app = Flask(__name__)



Data = {
        "Title":"YuriNovel"
        "Content":"Trang web cung cấp tiểu thuyết thể loại bách hợp miễn phí, được tạo bởi Tadashi Ringo vào năm 2020"
        "Author":"Tadashi Ringo"
        }



@app.route("/")
def index():
    return render_template("index.html",Title=Data['Title'])



if __name__=="__main__":
    app.run()
