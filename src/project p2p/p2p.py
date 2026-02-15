import socket, threading, os, time, sys, subprocess

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)
conn, addr = server.accept()
print("Connection established: type \\q to end convo")
"""while True:
    data = conn.recv(1024)  
    print("SENT:", data.decode())
    send = input("message: ")
    conn.sendall(send.encode())
    if send == "\\q":
        message = "12345554!"
        conn.sendall(message.encode())
        break"""

global message
global data
global history
global on
history = ""
message = ""
data = ""
mes = ""
on = True
def clear():
    os.system("cls" if os.name == "nt" else "clear")
    #subprocess.run("cls" if os.name == "nt" else "clear", shell=True)

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
    global on
    while on:
        global mes
        global history
        global data
        addto  = key()
        if addto:
            mes += addto.decode()
        if addto in back:
            mes=mes[:len(mes)-2]
        if addto in enter:
            if mes == "\\q\n" or data == "12345554!":
                conn.sendall("12345554!".encode())
                on = False
                #sys.exit()
            conn.sendall(mes.encode())
            history+="\nyou: "+mes
            mes=""

def inn():
    global history
    global data
    global on
    while on:
        data = conn.recv(1024).decode()
        history+=("\nthem: " + data)
def printhist():
    global on
    while on:
        global history
        global mes
        global data
        time.sleep(0.25)
        #clear()
        #print(history+"\nmessage: "+mes)
        #print("\x1b[H\x1b[2J", end="")
        sys.stdout.write("\033[H\033[J")   
        sys.stdout.write(history+'\n' + 'message: ' + mes)
        sys.stdout.flush()

sending = threading.Thread(target=out)
recieving = threading.Thread(target=inn)
printing = threading.Thread(target=printhist)

printing.start()
sending.start()
recieving.start()

printing.join()
sending.join()
recieving.join()


conn.close()
server.close()