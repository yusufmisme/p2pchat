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

if os.name == "nt":
    back = [b'\x08']
    enter = [b'\r']
    import msvcrt
    def key():
        if msvcrt.kbhit():
            return msvcrt.getch()
        else:
            return None
else:
    import termios, tty, fcntl
    back = [b'\x7f', b'\b']
    enter = [b'\n']
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd) # sets terminal in raw mode ig
    tty.setcbreak(fd)
    fcntl.fcntl(fd, fcntl.F_SETFL,
                fcntl.fcntl(fd, fcntl.F_GETFL) | os.O_NONBLOCK)
    
    def key():
        try:
            return sys.stdin.read(1)
        except:
            return None







def out():
    while True:
        global mes
        global history
        global data
        addto  = key()
        if addto:
            mes += addto.decode()
        if addto in back:
            mes=mes[:len(mes)-2]
        if addto in enter:
            client.sendall(mes.encode())
            history+="\nyou: "+mes
            mes=""
        if mes == "\\q" or data == "12345554!":
            break

def inn():
    global history
    global data
    while True:
        data = client.recv(1024).decode()
        history+=("\nthem:" + data)
        if mes == "\\q" or data == "12345554!":
            break
def printhist():
    while True:
        global history
        global mes
        global data
        time.sleep(0.25)
        #clear()
        #print(history+"\nmessage: "+mes)
        sys.stdout.write('\r' + 'message: ' + mes)
        sys.stdout.flush()
        if mes == "\\q" or data == "12345554!":
            break

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