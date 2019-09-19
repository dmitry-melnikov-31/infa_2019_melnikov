import turtle as tt

def mnogougolnik(n, a):
    for i in range(n):
        tt.forward(a)
        tt.left(360 / n)



tt.shape("turtle")
tt.pendown()

for i in range(10):
    mnogougolnik(i + 3, 20 + 20 * i)
    tt.penup()
    tt.left(180)
    tt.forward(10)
    tt.left(90)
    tt.forward(10)
    tt.left(90)
    tt.pendown()