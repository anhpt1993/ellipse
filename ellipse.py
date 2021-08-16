import turtle as t

def ellipse(r):
    for i in range(2):
        t.circle(r,90)
        t.circle(r/2,90)

count = 0
t.speed(100)

while True:
    t.right(45+count*5)
    t.penup()
    t.goto(count*5, count*-5)
    t.pendown()
    ellipse(200)
    count += 1
    if count > 72:
        break
    t.home()


t.hideturtle()
t.done()