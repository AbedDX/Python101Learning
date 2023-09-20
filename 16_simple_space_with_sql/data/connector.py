import sqlite3

create_table_sql = """CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname VARCHAR(20),
    lastname VARCHAR(50),
    email VARCHAR(50),
    phone VARCHAR(20)
)"""

get_contacts_sql = "SELECT * FROM contacts"

add_new_data_sql = "INSERT INTO contacts(firstname,lastname,email,phone) VALUES(?,?,?,?)"

def get_connection():
    conn = None
    try:
        conn = sqlite3.connect("database.db")
        return conn
    except:
        print("Failed to connect to database")
    return conn
    
def create_contact_table():
    conn = get_connection()
    if conn == None :
        return None
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print("Success in create contact table")
    except:
        print("Failed to create table")
        
def get_contacts():
    conn = get_connection()
    if conn == None:
        return None
    try:
        c = conn.cursor()
        contacts = c.execute(get_contacts_sql)
        return contacts.fetchall()
    except:
        print("Failed to get contacts")
        return None
        
def add_new_contact(data):
    conn = get_connection()
    if conn == None:
        return None
    try:
        c = conn.cursor()
        data_tuple=(data["firstname"],data["lastname"],data["email"],data["phone"])
        c.execute(add_new_data_sql,data_tuple)
        conn.commit()
        return "Success"
    except:
        print("Failed to add new contact")
        return None