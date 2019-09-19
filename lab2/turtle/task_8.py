import turtle as tt

tt.shape("turtle")
tt.pendown()
for i in range(100):
    tt.forward(10 + 10 * int(i / 2))
    tt.left(90)