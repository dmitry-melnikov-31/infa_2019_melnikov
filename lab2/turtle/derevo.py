import turtle as tt
alpha = 10
kef = 1
stvol = 50
t = tt.Turtle()
z = [(t, stvol)]
def run(z):
    t = tt.Turtle()
    t1 = tt.Turtle()
    t2 = tt.Turtle()
    t, a = z.pop(0)
    t.forward(a)
    t.left(alpha)
    t1 = t.clone()
    z.append((t1, a * kef))
    t.right(2 * alpha)
    t2 = t.clone()
    z.append((t2, a * kef))

    
    
for i in range(200):
    run(z)

t = tt.Turtle()
tt.exitonclick()

