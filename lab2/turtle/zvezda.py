import turtle as tt


def rebro(x, a):
    if (x == 0):
        tt.forward(a)
        return
    
    rebro(x - 1, a / 3)
    tt.left(60)
    rebro(x - 1, a / 3)
    tt.right(120)
    rebro(x - 1, a / 3)
    tt.left(60)
    rebro(x - 1, a / 3)

tt.penup()        
tt.goto(-300, 150)
tt.pendown()
for i in range(3):
    rebro(5, 500)
    tt.right(120)
tt.exitonclick()