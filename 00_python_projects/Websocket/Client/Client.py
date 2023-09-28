import socket
from flask import Flask, render_template, request

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("server", 15000))  # "server" is the Docker service name

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    client.send(message.encode())
    response = client.recv(1024).decode()
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)