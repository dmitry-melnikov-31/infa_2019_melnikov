import tkinter as tk
from random import randrange as rnd, choice
import time
root = tk.Tk()
root.geometry('800x600')
count = 20
colors = ['orange','yellow','green','blue']

canv = tk.Canvas(root,bg='white')
canv.pack(fill=tk.BOTH,expand=1)

def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)


class Pole:
    def __init__(self, x, y, k):
        self.p = Vector(x, y)
        self.k = k


class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    
    def add(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)
    
    def mul(self, a):
        return Vector(self.x * a, self.y * a)
    
    def show(self):
        print("(%s;%s)" % (self.x, self.y))





class Shar:
    def __init__(self, vx = 5, vy = 5, ax = 0, ay = 0):
        self.r = rnd(10, 20)
        self.m = (self.r ** 2)
        self.p = Vector(rnd(100, 700), rnd(100, 500))
        self.v = Vector(rnd(-5, 5), rnd(-5, 5))
        self.a = Vector(ax, ay)
        self.c = canv.create_oval(self.p.x-self.r,self.p.y-self.r,self.p.x+self.r,self.p.y+self.r,fill = choice(colors), width=0)
    
    def move(self):
        vmax = 10
        self.p = self.p.add(self.v)
        v = (self.v.x ** 2 + self.v.y ** 2) ** 0.5
        if v > vmax:
            col = rgb(0, 255, 0)
        else:
            col = rgb(0, round(255 / vmax * v), 255 - round(255 / vmax * v))
        canv.itemconfig(self.c, fill = col)
        canv.move(self.c, self.v.x, self.v.y)
    
    def ax(self):
        self.a.x = 0
        self.a.y = 0
        self.stena()
        self.trenie()
        self.another()
        self.pole(polep)
        self.v = self.v.add(self.a)
    
    def pole(self, pole):
        l = ((self.p.x - pole.p.x) ** 2 + (self.p.y - pole.p.y) ** 2) ** 0.5
        self.a.x = self.a.x + pole.k / l * (self.p.x - pole.p.x) / l
        self.a.y = self.a.y + pole.k / l * (self.p.y - pole.p.y) / l
    
    
    
    
    
    def stena(self):
        k = 2
        if self.p.x < self.r:
            self.a.x = self.a.x + (self.r - self.p.x) * k
        elif (800 - self.p.x) < self.r:
            self.a.x = self.a.x + (0 - self.r + (800 - self.p.x)) * k
        else:
            self.a.x = self.a.x + 0
        if self.p.y < self.r:
            self.a.y = self.a.y + (self.r - self.p.y) * k
        elif (600 - self.p.y) < self.r:
            self.a.y = self.a.y + (0 - self.r +  (600 - self.p.y)) * k
        else:
            self.a.y = self.a.y + 0
    
    def trenie(self):
        if (self.v.x > 5) or (self.v.x < -5):
            self.a.x = self.a.x + 0 - self.v.x * 0.01
        if (self.v.y > 5) or (self.v.x < -5):
            self.a.y = self.a.y + 0 - self.v.y * 0.01
    
    def another(self):
        global s, i, count
        k = 0.02
        for f in range(count):
            if i != f:
                l = ((self.p.x - s[f].p.x) ** 2 + (self.p.y - s[f].p.y) ** 2) ** 0.5
                if (self.r + s[f].r) > l:
                    self.a.x = self.a.x + (self.r + s[f].r - l) * (self.p.x - s[f].p.x) * k * s[f].m / self.m
                    self.a.y = self.a.y + (self.r + s[f].r - l) * (self.p.y - s[f].p.y) * k * s[f].m / self.m
            
            
            
s = []        
polep = Pole(400, 300, -50)
for i in range(count):        
    s.append(Shar())        

def update():
    for i in range(count):
        s[i].move()
        s[i].ax()
    root.after(30,update)
    
    
        
update()      
root.mainloop()