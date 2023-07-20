import sys
import socket

if len(sys.argv) != 3:
    print("Usage: python3 client.py <host> <port>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print("Connected to server at", host, "on port", port)

while True:
    message = input("Enter message: ")
    if message.lower() == "terminate":
        break

    client.send(message.encode())

client.close()

    