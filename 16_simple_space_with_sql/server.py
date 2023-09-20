from flask import Flask,jsonify,request
from data.connector import create_contact_table,get_contacts,add_new_contact

app = Flask(__name__,static_url_path="",static_folder="public")

create_contact_table()

@app.route("/api/contact",methods=["GET","POST"])
def fetch_contacts():
    if request.method == "GET":
        temp_contacts = get_contacts()
        if temp_contacts ==None:
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
    
app.run("127.0.0.1",port=8080)