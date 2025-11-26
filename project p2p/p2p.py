import socket
import turtle as t
import random
print("python b 2 ez bru, i wanna talk to memory directy")
def meoww():
    t.color("green")
    t.speed(0)
    t.circle(29)
    t.forward(58)
    t.circle(29)
    if random.randint(0,2) == 1:
        meow=80
    else:
        meow=100
    t.left(meow)
    t.forward(200)
    t.circle(29, 90)
    t.left(90)
    t.forward(29)
    t.back(29)
    t.right(90)
    t.circle(29, 90)
    t.forward(200)
while True:
    meoww()
    t.right(random.randint(0,180))
    t.forward(random.randint(0,300))
t.mainloop()