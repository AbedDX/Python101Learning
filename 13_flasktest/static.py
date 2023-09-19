from flask import Flask, send_file
app=Flask(__name__, static_url_path="",static_folder="/public")
@app.route("/")
def send_index():
    return send_file("./public/index1.html")

app.run("127.0.0.1", port=8080)





