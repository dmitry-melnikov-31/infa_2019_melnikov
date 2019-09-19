import turtle as tt

tt.shape("turtle")
tt.pendown()
for i in range(1000):
    tt.forward(1 + i / 10)
    tt.left(10)