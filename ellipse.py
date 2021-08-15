import turtle as t

def ellipse(r):
    for i in range(2):
        t.circle(r,90)
        t.circle(r/2,90)

t.right(45)
t.speed(5)
ellipse(200)
t.done()