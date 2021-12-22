from flask import Flask, render_template
import RPi.GPIO  as G
import time  as t
RED=4
BLUE=19
G.setmode(G.BCM)
G.setup(RED,G.OUT )
G.setup(BLUE,G.OUT )

app = Flask(__name__)

@app.route("/a")
def main_p():
    return render_template("main.html")


@app.route("/a/<col>/<op>")
def move(col,op):
    G.output(RED if int(col)==1 else BLUE,int(op))
    return json.dumps(('red' if int(col)==1 else 'blue')+'/'+op)

try:
    if __name__ == "__main__":
       app.run(host='0.0.0.0')
finally:
    G.cleanup()