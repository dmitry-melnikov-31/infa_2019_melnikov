import turtle as tt
tt.speed = 0

def zvezda(n, a):
    for i in range(n):
        tt.forward(a)
        tt.left(180 - 180 / n)

        
zvezda(11, 100)
tt.exitonclick()