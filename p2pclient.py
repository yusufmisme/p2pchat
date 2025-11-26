import socket
import threading
import os
import time
import sys

HOST = "192.168.1.190"
PORT = 5000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST,PORT))
global message
global data
global history
history = ""
message = ""
data = ""
mes = ""
def clear():
    os.system("cls" if os.name == "nt" else "clear")

print("Connection established: type \\q to end convo")

"""while True:
    message = input("message: ")
    client.sendall(message.encode())
    data = client.recv(1024)
    if message == "\\q" or data.decode() == "12345554!":
        break"""

def inn():
    global mes
    while True:
        addto  = sys.stdin.read(1)
        mes += addto
        if addto == '\n':
            client.sendall(mes.encode())

def out():
    global history
    while True:
        data = client.recv(1024).decode()
        history+=("\nthem:" + data)
        if message == "\\q" or data == "12345554!":
            break
def printhist():
    global history
    global mes
    while True:
        time.sleep(0.5)
        clear()
        print(history+"\nmessage: "+mes)

sending = threading.Thread(target=out)
recieving = threading.Thread(target=inn)
printing = threading.Thread(target=printhist)

printing.start()
sending.start()
recieving.start()

printing.join()
sending.join()
recieving.join()

client.close()