<<<<<<< HEAD
master的修改
=======
这是tom的修改
:wq
>>>>>>> Tom_bh
from flask import Flask, render_template, url_for

app = Flask(__name__)

# 注册路由
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/list")
def list_view():
    return render_template("child.html")


第一种方案

if __name__ == "__main__":
    app.run(debug=True)
