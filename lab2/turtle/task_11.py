import turtle as tt
tt.speed = 0
def circle(r):
    for i in range(60):
        tt.forward(2 * 3.1416 * r / 60)
        tt.left(6)

tt.shape("turtle")
tt.pendown()
for i in range(20):
    circle(50 + 10 * int(i / 2))
    tt.left(180)