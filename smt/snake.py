import tkinter as tk
from random import randrange as rnd, choice

def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)

root = tk.Tk()
root.title("Snake")
canv = tk.Canvas(root,bg='blue')
canv.pack(fill=tk.BOTH,expand=1)

class Map:
    def __init__(self, x = 30, y = 20, size = 20):
        self.size = size
        self.x = x
        self.y = y
        root.geometry(str(size * x) + 'x' + str(size * y))

    
class Snake:
    def __init__(self):
        self.pieces = []
        self.turn_queue = []
        self.pieces.append(Piece_of_snake(1, 1, m.size, is_head = True))
        self.pieces.append(Piece_of_snake(0, 1, m.size))
        self.headnumb = 0
        self.course = 'right'
        
    def move(self):
        if self.turn_queue != []:
            t = self.turn_queue.pop(0)
            if (t == 'up') and (self.course != 'down'):
                self.course = 'up'
            if (t == 'down') and (self.course != 'up'):
                self.course = 'down'
            if (t == 'right') and (self.course != 'left'):
                self.course = 'right'
            if (t == 'left') and (self.course != 'right'):
                self.course = 'left'
        xnew = self.pieces[self.headnumb].x
        ynew = self.pieces[self.headnumb].y
        
        if self.course == 'right':
            xnew += 1
        if self.course == 'left':
            xnew -= 1
        if self.course == 'up':
            ynew -= 1
        if self.course == 'down':
            ynew += 1
        
        if xnew == m.x:
            xnew = 0
        if ynew == m.y:
            ynew = 0
        if xnew == -1:
            xnew = m.x - 1
        if ynew == -1:
            ynew = m.y - 1
            
        self.pieces[self.headnumb].is_head = False
        canv.itemconfig(self.pieces[self.headnumb].id, fill = 'yellow')
        self.headnumb += 1    
        if self.headnumb == len(self.pieces):
            self.headnumb = 0
        self.pieces[self.headnumb].is_head = True
        self.pieces[self.headnumb].x = xnew
        self.pieces[self.headnumb].y = ynew
        canv.coords(self.pieces[self.headnumb].id, m.size * xnew, m.size * ynew, m.size * (xnew + 1), m.size * (ynew + 1)) 
        canv.itemconfig(self.pieces[self.headnumb].id, fill = 'green')
        self.eat()
        
        for i in self.pieces:
            if i != self.pieces[self.headnumb]:
                if (self.pieces[self.headnumb].x == i.x) and (self.pieces[self.headnumb].y == i.y):
                    g = tk.Label(text = "Длина твоей змеи " + str(len(self.pieces)), font = "Arial 14", bg = 'blue')
                    g.place(x = 70, y = 70)
                    for j in self.pieces:
                        canv.delete(j.id)
        
    def eat(self):
        global f
        if (f.x == self.pieces[self.headnumb].x) and (f.y == self.pieces[self.headnumb].y):
            canv.delete(f.id)
            f = Food()
            k = Piece_of_snake(self.pieces[self.headnumb - 1].x, self.pieces[self.headnumb - 1].y, m.size)
            self.pieces.insert(self.headnumb, k)
            self.headnumb += 1
        
    
    def turn_up(self, event):
        self.turn_queue.append('up')
    def turn_down(self, event):
        self.turn_queue.append('down')
    def turn_right(self, event):
        self.turn_queue.append('right')
    def turn_left(self, event):
        self.turn_queue.append('left')
        
        
        
        
        
class Piece_of_snake:
    def __init__(self, x, y, size, is_head = False):
        self.x = x
        self.is_head = is_head
        self.y = y
        self.size = size
        col = 'yellow'
        if self.is_head:
            col = 'green'
        self.id = canv.create_rectangle(size * x, size * y, size * (x + 1), size * (y + 1), fill = col, width = 0)

class Food:
    def __init__(self, x = -1, y = -1):
        if x == -1:
            x = rnd(0, m.x)
        if y == -1:
            y = rnd(0, m.y)
        self.x = x
        self.y = y
        self.size = 0
        self.id = canv.create_oval(m.size * x, m.size * y, m.size * (x + 1), m.size * (y + 1), fill = 'red', width = 0)
    
    def pulse(self):
        self.size += 1
        if self.size == 100:
            self.size = 0
        canv.coords(self.id,
                    m.size * self.x + (m.size * (self.size % 2) * 0.2),
                    m.size * self.y + (m.size * (self.size % 2) * 0.2),
                    m.size * (self.x + 1) - (m.size * (self.size % 2) * 0.2),
                    m.size * (self.y + 1) - (m.size * (self.size % 2) * 0.2))
        
    
  
    
def update():
    s.move()
    f.pulse()
    root.after(100, update)
        
    
m = Map()    
s = Snake()
f = Food()  


root.bind('<Left>', s.turn_left)
root.bind('<Right>', s.turn_right)
root.bind('<Up>', s.turn_up)
root.bind('<Down>', s.turn_down)
update()    
root.mainloop()