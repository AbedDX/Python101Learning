from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def contact():
    return render_template("contact.html")
    
@app.route("/result",methods=['GET','POST'])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html",result=result)

app.run("127.0.0.1", port=8080)