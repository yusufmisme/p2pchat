import socket
HOST = "192.168.137.1"
PORT = 5000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))
while True:
    message = input("message: ")
    client.sendall(message.encode())
    data = client.recv(1024)
    if data.decode() == "12345554!":
        break
    print("SENT:", data.decode())
client.close()