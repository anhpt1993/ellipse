import turtle as t
import random

def ellipse(r):
    for i in range(2):
        t.circle(r,90)
        t.circle(r/2,90)

count = 0
t.speed(100)
colors = ["blue", "orange", "green", "red", "purple", "brown", "pink", "gray", "olive", "cyan"]
while True:
    t.right(45+count*5)
    t.pendown()
    t.pencolor(random.choice(colors))
    ellipse(200)
    count += 1
    if count > 72:
        break
    t.home()

t.hideturtle()
t.done()