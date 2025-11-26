import socket
HOST = "192.168.137.1"
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)
conn, addr = server.accept()
while True:
    data = conn.recv(1024)  
    print("SENT:", data.decode())
    send = input("send? ")
    if send == "y":
        message = input("what: ")
        conn.sendall(message.encode())
    elif send == "n":
        message = "12345554!"
        conn.sendall(message.encode())
        break
conn.close()
server.close()