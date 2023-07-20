import sys
import socket
import threading

clients = []

if len(sys.argv) != 2:
    print("Usage: python3 server.py <port>")
    sys.exit(1)

port = int(sys.argv[1])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', port))
server.listen(1)
print("Server is listening on port", port)

def broadcast(clients, message):
    for connection in clients:
        try:
            connection.send(message)
        except socket.error:
            clients.remove(connection)

def recive(connection, clients):
    while True:
        data = connection.recv(1024)
        broadcast(clients, data)
        if not data:
            break
        print("From connected client :", data.decode())


while True:
    connection, address = server.accept()
    print("Client connected from", address)
    clients.append(connection)
    thread = threading.Thread(target=recive , args=(connection, clients))
    thread.start()

