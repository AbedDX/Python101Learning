import socket
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("hostname", 15000))  # Replace "server" with the actual server hostname or IP address
    client.send(message.encode())
    response = client.recv(1024).decode()
    client.close()
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
