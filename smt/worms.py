import tkinter as tk
from random import randrange as rnd, choice
import time
import math
root = tk.Tk()
root.geometry('800x600')
colors = ['orange','yellow','green','blue']

canv = tk.Canvas(root,bg='white')
canv.pack(fill=tk.BOTH,expand=1)

class Bullet():
    def __init__(self, x, y, vx, vy):
        self.r = 5
        self.it = 0
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = 'red', width = 0)
        
    def move(self):
        global ground, bullets, worms
        canv.move(self.id, self.vx, -self.vy)
        self.x += self.vx
        self.y -= self.vy
        self.vy -= 1
        self.it += 1
        if ground.h[self.x][1] < self.y:
            canv.delete(self.id)
            ground.boom(self.x, self.y, 25)
            bullets.pop(0)
            return
        if self.it > 5:    
            for w in worms:
                l = ((self.x - w.x) ** 2 + (self.y - (w.y - w.r)) ** 2) ** 0.5
                if l < self.r + w.r:
                    canv.delete(self.id)
                    ground.boom(self.x, self.y, 25)
                    bullets.pop(0)
                    return


class Worm():
    def __init__(self, x = 100, ori = True):
        global ground
        self.hp = 100
        self.x = x
        self.y = ground.h[self.x][1]
        self.r = 15
        self.hp_text = canv.create_text(self.x, self.y - self.r * 3, text=str(self.hp), font='28')
        self.ori = ori
        self.v = 0
        self.alpha = math.pi / 6
        self.id = canv.create_oval(self.x - self.r, self.y - 2 * self.r, self.x + self.r, self.y, fill = 'green', width = 0)
        self.aim = canv.create_oval(self.x + (2 * int(self.ori) - 1) * 2 * self.r * math.cos(self.alpha) - 3,
                                    self.y - self.r - 2 * self.r * math.sin(self.alpha) - 3,
                                    self.x + (2 * int(self.ori) - 1) * 2 * self.r * math.cos(self.alpha) + 3,
                                    self.y - self.r - 2 * self.r * math.sin(self.alpha) + 3,
                                    fill = 'blue', width = 0)

    
    def moving(self):
        h1 = self.y
        self.x += self.v
        self.y = ground.h[self.x][1]
        h2 = self.y
        if h2 - h1 > 2 * self.r:
            self.damage((h2 - h1 - 2 * self.r) // 4)
        if h1 - h2 > 2 * self.r:
            self.x -= self.v
            self.y = ground.h[self.x][1]
        canv.coords(self.id, self.x - self.r, self.y - 2 * self.r, self.x + self.r, self.y)
        canv.coords(self.hp_text, self.x, self.y - self.r * 3)
        canv.itemconfig(self.hp_text, text = str(self.hp))
        canv.coords(self.aim, self.x + (2 * int(self.ori) - 1) * 2 * self.r * math.cos(self.alpha) - 3,
                              self.y - self.r - 2 * self.r * math.sin(self.alpha) - 3,
                              self.x + (2 * int(self.ori) - 1) * 2 * self.r * math.cos(self.alpha) + 3,
                              self.y - self.r - 2 * self.r * math.sin(self.alpha) + 3,)
    
    def damage(self, x):
        self.hp -= round(x)
        if self.hp < 0:
            self.hp = 0
    def start_moving_right(self, event):
        self.v = 1
        self.ori = True
    def start_moving_left(self, event):
        self.v = -1
        self.ori = False
    def end_moving(self, event):
        self.v = 0
    def aim_up(self, event):
        self.alpha += math.pi / 4 / 1.5 * 0.03 * 2
        if self.alpha > math.pi / 2:
            self.alpha = math.pi / 2
    def aim_down(self, event):
        self.alpha -= math.pi / 4 / 1.5 * 0.03 * 2
        if self.alpha < - math.pi / 2:
            self.alpha = - math.pi / 2
    def fire(self, event):
        global bullets, activ, worms, ground
        ground.turn += 1
        self.v = 0
        activ += 1
        if activ == len(worms):
            activ = 0
        bullets.append(Bullet(self.x, self.y - self.r, (2 * int(self.ori) - 1) * round(20 * math.cos(self.alpha)),
                                                       round(20 * math.sin(self.alpha))))
        
        
class Ground():
    def __init__(self):
        self.turn = 1
        z = 300
        self.id = 0
        self.h = []
        for i in range(800 + 1):
            z += rnd(-1, 1 + 1)
            self.h.append((i, z))
    def no_show(self):
        canv.delete(self.id)
    def show(self, color = 'yellow'):
        self.h.append((800, 600))
        self.h.append((0, 600))
        self.id = canv.create_polygon(self.h, fill = color)
        self.h.pop(-1)
        self.h.pop(-1)
    def boom(self, x, y, r):
        global worms
        for w in worms:
            l = ((w.x - x) ** 2 + (w.y - y) ** 2) ** 0.5
            if l < r:
                w.damage(r - l)
        
        for i in range(800 + 1):
            if (x - r < i) and (x + r > i):
                hn =  y + ((r ** 2) - (x - i) ** 2) ** 0.5
                if hn > self.h[i][1]:
                    self.h[i] = (i, hn)

def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)
def cl(event):
    root.destroy()
bullets = []
worms = []
def update(event = ''):
    global activ, worms
    for w in worms:
        w.moving()
    root.bind('<KeyPress-d>', worms[activ].start_moving_right)
    root.bind('<KeyPress-a>', worms[activ].start_moving_left)
    root.bind('<KeyRelease-d>', worms[activ].end_moving)
    root.bind('<KeyRelease-a>', worms[activ].end_moving)
    root.bind('<KeyPress-w>', worms[activ].aim_up)
    root.bind('<KeyPress-s>', worms[activ].aim_down)
    root.bind('<KeyPress-Return>', worms[activ].fire)
    root.bind('<KeyPress-Escape>', cl)
    for q in range(len(worms)):
        if worms[q].hp < 1:
            canv.delete(worms[q].id)
            canv.delete(worms[q].aim)
            worms.pop(q)
    ground.no_show()
    ground.show()
    
    for b in bullets:
        b.move()
    root.after(30,update)
ground = Ground()
ground.show()
worms.append(Worm(100, True))  
worms.append(Worm(700, False))        
activ = 0
update()  
root.mainloop()