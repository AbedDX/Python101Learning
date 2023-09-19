from flask import Flask,render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html",title="Welcome",username="Erno")
    
@app.route("/if")
def if_example():
    return render_template("if.html",title="If example",username="Erno")
 
@app.route("/if/<username>")
def if_username(username):
    name = escape(username)
    return render_template("if.html",title="If example 2",username=name)

@app.route("/loop")
def loop():
    members= ["Abdalle","Khadar","Iljas","Hibak","Kaltun"]
    return render_template("loop.html",title="Loops",members=members)
    
app.run("127.0.0.1", port=8080)