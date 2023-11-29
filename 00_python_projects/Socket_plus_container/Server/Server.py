import socket

def server():
    # get hostname
    host = socket.gethostname()
    port = 15000
    
    server_socket = socket.socket()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host,port))
    server_socket.listen(5)
    conn, address = server_socket.accept()
    print("Connection from address",str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From user:",data)
        data = input(" -> ")
        conn.send(data.encode())

    conn.close()

if __name__ == "__main__":
	server() 