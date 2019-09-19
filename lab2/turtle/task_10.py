import turtle as tt

def circle(r):
    for i in range(360):
        tt.forward(2 * 3.1416 * r / 360)
        tt.left(1)

tt.shape("turtle")
tt.pendown()
for i in range(6):
    circle(100)
    tt.left(60)