import threading
import os
user_text = None

def input_thread():
    global user_text
    while True:
        user_text = input("> ")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

t = threading.Thread(target=input_thread, daemon=True)
t.start()

# Main program keeps running!

clear()
print("Main loop is still running...")
if user_text is not None:
    print("You typed:", user_text)
    user_text = None
# do other work here
