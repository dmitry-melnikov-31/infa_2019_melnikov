import tkinter as tk
from random import randrange as rnd, choice

root = tk.Tk()

canv = tk.Canvas(root,bg='white')
canv.pack(fill=tk.BOTH,expand=1)

def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)

class Map():
    def __init__(self, x, y, size = 5):
        self.x = x
        self.y = y
        self.size = size
        self.p = []
        root.geometry(str(self.size * x) + 'x' + str(self.size * y))
        for i in range(x):
            self.p.append([])
            for j in range(y):
                self.p[i].append(Point(i, j, self.size))

    def up(self):
        for i in self.p:
            for j in i:
                j.new_color()
        for i in self.p:
            for j in i:
                j.col = j.newcol
                j.show()
    def summ(self):
        s = 0
        for i in self.p:
            for j in i:
                s += j.col
        return s
                
                
class Point():
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.life = bool(rnd(0, 2))
        self.col = 255 * int(self.life)
        self.newcol = self.col
        self.id = canv.create_rectangle(size * self.x, size * self.y, size * self.x + size, size * self.y + size, 
                                        fill = rgb(0, round(self.col), round(255 - self.col)), 
                                        width = 0)
    def show(self):    
        canv.itemconfig(self.id, fill = rgb(0, round(self.col), round(255 - self.col)))
    def new_color(self):
        k = 0
        z = 0
        if (self.x != 0) and (self.y != 0):
            z += m.p[self.x - 1][self.y - 1].col
            k += 1
        if (self.x != 0):
            z += m.p[self.x - 1][self.y].col
            k += 1
        if (self.x != 0) and (self.y != m.y - 1):
            z += m.p[self.x - 1][self.y + 1].col
            k += 1
        if (self.x != m.x - 1) and (self.y != m.y - 1):    
            z += m.p[self.x + 1][self.y + 1].col
            k += 1
        if (self.x != m.x - 1) and (self.y != 0):
            z += m.p[self.x + 1][self.y - 1].col
            k += 1
        if (self.x != m.x - 1):
            z += m.p[self.x + 1][self.y].col
            k += 1
        if (self.y != m.y - 1):    
            z += m.p[self.x][self.y + 1].col
            k += 1
        if (self.y != 0):    
            z += m.p[self.x][self.y - 1].col
            k += 1
        if (self.col == 0):
            if (z == 255 * 3):
                self.newcol = 255
        if (self.col == 255):
            if (z != 255 * 2) and (z != 255 * 3):
                self.newcol = 0


def update():
    m.up()
    print(m.summ() // 255)
    root.after(30, update)

    
m = Map(60, 40)
update()
root.mainloop()