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
