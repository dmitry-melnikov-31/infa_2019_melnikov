import tkinter as tk
from random import randrange as rnd, choice

def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)

root = tk.Tk()
root.title("Snake")
canv = tk.Canvas(root,bg='blue')
canv.pack(fill=tk.BOTH,expand=1)

class Map():
    def __init__(self, x = 30, y = 20, size = 10):
        self.size = size
        self.x = x
        self.y = y
        root.geometry(str(size * x) + 'x' + str(size * y))

    
class Snake():
    def __init__(self):
        self.pieces = []
        self.pieces.append(Piece_of_snake(1, 1, 10, is_head = True))
        self.pieces.append(Piece_of_snake(0, 1, 10))
        self.pieces.append(Piece_of_snake(0, 1, 10))
        self.pieces.append(Piece_of_snake(0, 1, 10))
        self.pieces.append(Piece_of_snake(0, 1, 10))
        self.pieces.append(Piece_of_snake(0, 1, 10))
        self.pieces.append(Piece_of_snake(0, 1, 10))
        self.pieces.append(Piece_of_snake(0, 1, 10))
        self.pieces.append(Piece_of_snake(0, 1, 10))
        self.pieces.append(Piece_of_snake(0, 1, 10))
        self.course = 'right'
        
    def move(self):
        for i in range(len(self.pieces)):
            if self.pieces[i].is_head:
                headnumb = i
        xnew = self.pieces[headnumb].x
        ynew = self.pieces[headnumb].y
        
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
            
        self.pieces[headnumb].is_head = False
        canv.itemconfig(self.pieces[headnumb].id, fill = 'yellow')
        headnumb += 1    
        if headnumb == len(self.pieces):
            headnumb = 0
        self.pieces[headnumb].is_head = True
        self.pieces[headnumb].x = xnew
        self.pieces[headnumb].y = ynew
        canv.coords(self.pieces[headnumb].id, m.size * xnew, m.size * ynew, m.size * (xnew + 1), m.size * (ynew + 1)) 
        canv.itemconfig(self.pieces[headnumb].id, fill = 'red')
    
    def turn_up(self, event):
        if self.course != 'down':
            self.course = 'up'
    def turn_down(self, event):
        if self.course != 'up':
            self.course = 'down'
    def turn_right(self, event):
        if self.course != 'left':
            self.course = 'right'
    def turn_left(self, event):
        if self.course != 'right':
            self.course = 'left'
        
        
        
        
        
class Piece_of_snake():
    def __init__(self, x, y, size, is_head = False):
        self.x = x
        self.is_head = is_head
        self.y = y
        self.size = size
        col = 'yellow'
        if self.is_head:
            col = 'red'
        self.id = canv.create_rectangle(size * x, size * y, size * (x + 1), size * (y + 1), fill = col, width = 0)

    
    
    
    
def update():
    s.move()
    root.after(200, update)
        
    
m = Map()    
s = Snake()
root.bind('<Left>', s.turn_left)
root.bind('<Right>', s.turn_right)
root.bind('<Up>', s.turn_up)
root.bind('<Down>', s.turn_down)
update()    
root.mainloop()