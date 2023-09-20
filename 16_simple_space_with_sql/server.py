from flask import Flask,jsonify,request,send_file
from data.connector import create_contact_table,get_contacts,add_new_contact,remove_contact,edit_contact

app = Flask(__name__,static_url_path="",static_folder="public")

create_contact_table()

@app.route("/")
@app.route("/index")
def index():
    return send_file("public/index.html")

@app.route("/api/contact",methods=["GET","POST"])
def fetch_contacts():
    if request.method == "GET":
        temp_contacts = get_contacts()
        if temp_contacts == None:
            return "Internal Server Error",500
        contacts = []
        for i in range(len(temp_contacts)):
            contacts.append({
                "id":temp_contacts[i][0],
                "firstname":temp_contacts[i][1],
                "lastname":temp_contacts[i][2],
                "email":temp_contacts[i][3],
                "phone":temp_contacts[i][4]
            })
        return jsonify(contacts)
    else:
        data = request.json
        print(data)
        success = add_new_contact(data)
        if success == None:
            return "Internal Server Error",500
        return "Success",201

@app.route("/api/contact/<int:id>",methods=["DELETE","PUT"])
def handle_remove_and_edit(id):
    if request.method == "DELETE":
        success = remove_contact(id)
        if success == None:
            return "Internal Server Error",500
        return "Success",200
    else:
        data = request.json
        success = edit_contact(id)
        if success == None:
            return "Internal Server Error",500
        return "Success",200
    
app.run("127.0.0.1",port=8080)