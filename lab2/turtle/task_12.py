import turtle as tt


def duga(r):
    for i in range(30):
        tt.forward(2 * 3.1416 * r / 60)
        tt.left(6)

tt.shape("turtle")
tt.pendown()
for i in range(20):
    duga(20)
    duga(5)