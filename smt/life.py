import tkinter as tk
from random import randrange as rnd, choice
mx = 50
my = 50

def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)

class Map():
    def __init__(self, x, y, size = 10):
        self.x = x
        self.y = y
        self.age = 0
        self.size = size
        self.p = []
        root.geometry(str(self.size * x + 200) + 'x' + str(self.size * y))
        for i in range(x):
            self.p.append([])
            for j in range(y):
                self.p[i].append(Point(i, j, self.size))

    def up(self):
        self.age += 1
        for i in self.p:
            for j in i:
                j.new_color()
        for i in self.p:
            for j in i:
                if j.col != j.newcol: 
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
    if playing:
        m.up()
        surv_count.config(text = "alive " + str(m.summ() // 255))
        age_count.config(text = "age " + str(m.age))
    root.after(30, update)

root = tk.Tk()
root.title("Comedy")
canv = tk.Canvas(root,bg='yellow')
canv.pack(fill=tk.BOTH,expand=1)
playing = False

def one_era(): 
    m.up()
    surv_count.config(text = "alive " + str(m.summ() // 255))
    age_count.config(text = "age " + str(m.age))
def start_playing():
    global playing
    playing = True
    return
def end_playing():
    global playing
    playing = False
    return
def exite(event):
    root.destroy()
def exite():
    root.destroy()
def restart():
    global m
    for i in m.p:
        for j in i:
           canv.delete(j.id)
    m = Map(mx, my)
    return


xdraw = 0
ydraw = 0

def drawing(event):
    global m, mx, my, draw, xdraw, ydraw
    if draw:
        x = event.x // m.size
        y = event.y // m.size
        if (xdraw != x) or (ydraw != y):
            xdraw = x
            ydraw = y
            if (x < mx) and (y < my) and (x >= 0) and (y >= 0):
                if m.p[x][y].col == 0:
                    m.p[x][y].col = 255
                else:
                    m.p[x][y].col = 0
                m.p[x][y].newcol = m.p[x][y].col
                m.p[x][y].show()

def start_drawing(event):
    global draw, xdraw, ydraw
    xdraw = 0
    ydraw = 0
    draw = True
    return
def end_drawing(event):
    global draw, xdraw, ydraw
    xdraw = 0
    ydraw = 0
    draw = False
    return
def clear():
    for i in m.p:
        for j in i:
            j.col = 0
            j.newcol = 0
            j.show()



m = Map(mx, my)

start_button = tk.Button(root, text = "start", font = "Arial 14", width = 8, height = 1, bg = 'yellow', command = start_playing)
start_button.place(x = m.size * m.x, y = 0)

end_button = tk.Button(root, text = "stop", font = "Arial 14", width = 8, height = 1, bg = 'yellow', command = end_playing)
end_button.place(x = m.size * m.x + 100, y = 0)

one_era_button = tk.Button(root, text = "era", font = "Arial 14", width = 8, height = 1, bg = 'yellow', command = one_era)
one_era_button.place(x = m.size * m.x, y = 80)

restart_button = tk.Button(root, text = "restart", font = "Arial 14", width = 8, height = 1, bg = 'yellow', command = restart)
restart_button.place(x = m.size * m.x + 100, y = 40)

surv_count = tk.Label(text = '', font = "Arial 14", width = 9, bg = 'yellow')
surv_count.place(x = m.size * m.x, y = 160)

age_count = tk.Label(text = '', font = "Arial 14", width = 9, bg = 'yellow')
age_count.place(x = m.size * m.x, y = 190)

clear_button = tk.Button(root, text = "clear", font = "Arial 14", width = 8, height = 1, bg = 'yellow', command = clear)
clear_button.place(x = m.size * m.x, y = 40)

exit_button = tk.Button(root, text = "exit", font = "Arial 14", width = 8, height = 1, bg = 'yellow', command = exit)
exit_button.place(x = m.size * m.x + 100, y = 80)

draw = False
root.bind('<KeyPress-Escape>', exite)
canv.bind('<ButtonPress-1>', start_drawing)
canv.bind('<ButtonRelease-1>', end_drawing)
canv.bind('<Motion>', drawing)
canv.bind('<ButtonPress-1>', drawing, '+')
update()
root.mainloop()