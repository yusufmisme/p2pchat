import socket
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)
conn, addr = server.accept()
print("Connection established: type \\q to end convo")
while True:
    data = conn.recv(1024)  
    print("SENT:", data.decode())
    send = input("message: ")
    conn.sendall(send.encode())
    if send == "\\q":
        message = "12345554!"
        conn.sendall(message.encode())
        break
conn.close()
server.close()