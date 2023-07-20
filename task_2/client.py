import sys
import socket

if len(sys.argv) != 4:
    print("Usage: python3 client.py <host> <port> <actor>")
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])
actor = sys.argv[3]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print("Connected to server at", host, "on port", port)


if actor.upper() == "PUBLISHER":
    while True:
        message = input("Enter message: ")
        if message.lower() == "terminate":
            break
        client.send(message.encode())

elif actor.upper() == "SUBSCRIBER":
    while True:
        data = client.recv(1024)
        if not data:
            break
        print("From connected PUBLISHER:", data.decode())

client.close()

    