from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def main_p():
    return render_template("main.html")

@app.route("/a/<num>")
def move(num):
    if num=='err': return render_template("err.html")
    else: return render_template("get.html",data=num)

if __name__ == "__main__":
    app.run(host='0.0.0.0')