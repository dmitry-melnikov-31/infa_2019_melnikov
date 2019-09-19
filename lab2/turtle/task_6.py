import turtle as tt

def pavuk(n):
    tt.shape("turtle")
    tt.pendown()
    for i in range(n):
        tt.forward(100)
        tt.stamp()
        tt.backward(100)
        tt.left(360 / n)
        
pavuk(20)