import sys
import socket
import threading

clients = []

if len(sys.argv) != 2:
    print("Usage: python3 server.py <port>")
    sys.exit(1)

port = int(sys.argv[1])

def broadcast(clients, topic, message):
    for connection, client_topic in clients:
        if client_topic == topic:
            try:
                connection.send(message)
            except socket.error:
                clients.remove((connection, client_topic))
            

def recive(connection, clients, topic):
    while True:
        data = connection.recv(1024)
        broadcast(clients, topic, data)
        if not data:
            break
        print("From connected client :", data.decode())


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', port))
server.listen(1)
print("Server is listening on port", port)

while True:
    connection, address = server.accept()
    topic = connection.recv(1024).decode()
    print("Client connected from on [", topic, "]", address)
    
    clients.append((connection, topic))
    
    thread = threading.Thread(target=recive , args=(connection, clients, topic))
    thread.start()
