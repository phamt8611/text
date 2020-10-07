from flask import Flask, render_template


app = Flask(__name__)



Data = {
        "Color":{
            "Title":"color:red"
            },
        "Styles":{
            "Menu":"margin: 6px;padding: 2px;display: inline-block;color: red"
            }
        }



@app.route("/")
def index():
    return render_template(
            "index.html",
            title='Trang Chủ',
            ColorTitle=Data['Color']['Title'],
            StyleMenu=Data['Styles']['Menu']
            )
@app.route("/find")
def find():
    return render_template("find.html",
            title='Tìm Kiếm',
            ColorTitle=Data['Color']['Title'],
            StyleMenu=Data['Styles']['Menu']
            )
@app.route("/forum")
def forum():
    return render_template("forum.html",
            title='Tìm Kiếm',
            ColorTitle=Data['Color']['Title'],
            StyleMenu=Data['Styles']['Menu']
            )
@app.route("/lienhe")
def lienhe():
    return render_template("lienhe.html",
            title='Liên Hệ',
            ColorTitle=Data['Color']['Title'],
            StyleMenu=Data['Styles']['Menu']
            )
@app.route("/donate")
def donate():
    return render_template("donate.html",
            title='Donate',
            ColorTitle=Data['Color']['Title'],
            StyleMenu=Data['Styles']['Menu']
            )
if __name__=="__main__":
    app.run()
