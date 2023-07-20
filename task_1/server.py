import sys
import socket

if len(sys.argv) != 2:
    print("Usage: python3 server.py <port>")
    sys.exit(1)

port = int(sys.argv[1])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', port))
server.listen(1)
print("Server is listening on port", port)

connection, address = server.accept()
print("Client connected from", address)

while True:
    data = connection.recv(1024)
    if not data:
        break
    print("From connected client :", data.decode())


connection.close()    
