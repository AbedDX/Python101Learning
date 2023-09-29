import socket
from flask import Flask, render_template

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 15000))
server.listen(5)

print("Server is listening...")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def handle_client(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(f"Client: {message}")
        response = input("You: ")
        client_socket.send(response.encode())
    client_socket.close()

@app.route('/chat', methods=['POST'])
def chat():
    client_socket, client_address = server.accept()
    print(f"Connection from {client_address}")
    handle_client(client_socket)
    return "Chat finished."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 80)
