from flask import Flask, render_template


app = Flask(__name__)



Data = {
        "Title":"YuriNovel",
        "Content":"Nền tảng văn học mạng, cung cấp truyện bách hợp miễn phí, gồm các thể loại đồng nhân, đô thị, nhị thứ nguyên, tam thứ nguyên",
        "Author":"Tadashi Ringo",
        "Charset":"UTF-8",
        "Keywords":"truyện bách hợp, truyện yuri, Yuri, Novel, Tadashi Ringo, Lesbian",
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
            Title=Data['Title'],
            Description=Data['Content'],
            Keywords=Data['Keywords'],
            Charset=Data['Charset'],
            Author=Data['Author'],
            ColorTitle=Data['Color']['Title'],
            StyleMenu=Data['Styles']['Menu']
            )
if __name__=="__main__":
    app.run()
