import tkinter as tk
import numpy as np
import sys
from random import randrange as rnd, choice
root = tk.Tk()
courses = ['up', 'down', 'right', 'left']
root.title("Box of tanks")
canv = tk.Canvas(root,bg='white')
canv.pack(fill=tk.BOTH,expand=1)
vision = False
if len(sys.argv) != 1:
    if sys.argv[1] == 'vis':
        vision = True



def crossingover(a, b):
    c = []
    for i in range(len(a)):
        r = rnd(0, 2)
        if r == 0:
            c.append(a[i])
        else:
            c.append(b[i])
    return c


def weights_update():
    file = open('rezults.csv', 'r')
    rezults = file.read()
    file.close()
    ar = []
    for i in rezults.split('\n'):
        ar.append(i.split(','))
    ar.pop(-1)
    z = []
    for i in range(len(ar)):
        z.append((ar[i][0], ar[i][1]))
    dtype = [('number', int), ('points', int)]
    rez = np.array(z, dtype = dtype)
    rez = np.sort(rez, order = 'points')
    rez = rez[30:50]
    print(rez)
    winners = []
    for i in rez:
        winners.append(i[0])
    winners.sort()
    file = open('tanks_weights.csv', 'r')
    weights = file.read()
    file.close()
    ar = []
    for i in weights.split('\n'):
        ar.append(i.split(','))
    ar.pop(-1)
    new_weights = []
    for i in winners:
        new_weights.append(ar[i])
    for i in range(20):
        new_weights.append(crossingover(new_weights[i],new_weights[i + 1]))
    
    for i in range(5):
        sss = []
        for j in range(9):
            sss.append(str(rnd(-100, 101)))
        new_weights.append(sss)
        
    for i in range(5):
        new_weights.append(crossingover(new_weights[i],new_weights[i + 40]))
                       
    file = open('tanks_weights.csv', 'w')
    for i in range(len(new_weights)):
        for j in range(len(new_weights[i])):
            file.write(new_weights[i][j])
            if j != len(new_weights[i]) - 1:
                file.write(',')
        file.write('\n')
    file.close()



def exit(event):
    rezults = open('rezults.csv', 'w')
    for t in m.tanks:
        rezults.write(str(t.number) + ',' + str(t.points) + '\n')
    for t in m.dead_tanks:
        rezults.write(str(t.number) + ',' + str(t.points) + '\n')
    rezults.close()
    weights_update()
    root.destroy()

def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)

class Map:
    def __init__(self, x = 200, y = 130, size = 3, bullets_speed = 5):
        self.x = x
        self.y = y
        self.size = size
        self.bullets = []
        self.tanks = []
        self.dead_tanks = []
        self.age = 0
        self.tanks_max_charges = 3
        self.tanks_start_lifes = 3
        self.bullets_speed = bullets_speed
        root.geometry(str(self.x * self.size) + 'x' + str(self.y * self.size))
        
    def update(self):
        self.age += 1 
        if self.age % self.bullets_speed == 0:
            for t in self.tanks:
                t.tank_update()
                if t.charges != self.tanks_max_charges:
                    t.charge_part += 1
                    if t.charge_part == 5:
                        t.charge_part = 0
                        t.charges += 1
        for b in self.bullets:
            b.bullet_update() 
        self.colision()
        if self.age == 3000:
            exit('')
        root.after(1, self.update)
    
    def spaun_bots(self):
        global weights
        
        for i in range(50):
            self.tanks.append(Tank(m, weights[i].split(','), number = i, x = rnd(1, self.x - 1), y = rnd(1, self.y - 1), course = choice(courses)))
    
    def colision(self):
        for b in self.bullets:
            z = True
            for t in self.tanks:
                if (b.parent != t) and ((t.x - b.x) ** 2 < 2) and ((t.y - b.y) ** 2 < 2):
                    t.lifes -= 1
                    if t.lifes == 0:
                        b.parent.points += 300
                    b.parent.points += 100
                    if z:
                        b.destroy()
                        z = False

class Bullet: #____________________________________________________________________________________________________________________________
    def __init__(self, world, x, y, course, parent):
        self.x = x
        self.y = y
        self.course = course
        self.parent = parent
        self.world = world
        if vision:
            self.id = canv.create_oval((self.x  + 0.1)* self.world.size, (self.y + 0.1)* self.world.size,
                                            (self.x + 0.9) * self.world.size, (self.y + 0.9) * self.world.size, fill = 'red', width = 0)
    
    def bullet_update(self):
        self.move()
        if (self.x < 0) or (self.y < 0) or (self.x > m.x - 1) or (self.y > m.y - 1):
            self.destroy()
        self.show()
    
    def show(self):
        if vision:
            canv.coords(self.id, (self.x  + 0.1)* self.world.size, (self.y + 0.1)* self.world.size,
                    (self.x + 0.9) * self.world.size, (self.y + 0.9) * self.world.size)
    
    def move(self):
        if self.course == 'up':
            self.y -= 1
        if self.course == 'down':
            self.y += 1
        if self.course == 'left':
            self.x -= 1
        if self.course == 'right':
            self.x += 1
    
    def destroy(self):
        self.world.bullets.remove(self)
        if vision:
            canv.delete(self.id)
    
    
class Tank: #_____________________________________________________________________________________________________________________________
    def __init__(self, world, w, number = 0, x = 10, y = 10, course = 'right', ii = 'True'):
        self.x = x
        self.y = y
        self.points = 0
        self.number = number
        self.course = course
        self.ii = ii
        self.turning_left = False
        self.turning_right = False
        self.moving = False
        self.fireing = False
        self.w = []
        for i in w:
            self.w.append(int(i))
        self.world = world
        self.lifes = self.world.tanks_start_lifes
        self.charges = self.world.tanks_max_charges
        self.charge_part = 0
        if vision:
            self.centre = canv.create_rectangle(self.x * self.world.size, self.y * self.world.size,
                                            (self.x + 1) * self.world.size, (self.y + 1) * self.world.size, fill = 'black', width = 0)
            self.gun = canv.create_rectangle(self.x * self.world.size, self.y * self.world.size,
                                        (self.x + 1) * self.world.size, (self.y + 1) * self.world.size, fill = 'black', width = 0)
            self.left_bort = canv.create_rectangle(self.x * self.world.size, self.y * self.world.size,
                                            (self.x + 1) * self.world.size, (self.y + 1) * self.world.size, fill = 'black', width = 0)
            self.right_bort = canv.create_rectangle(self.x * self.world.size, self.y * self.world.size,
                                            (self.x + 1) * self.world.size, (self.y + 1) * self.world.size, fill = 'black', width = 0)
            self.left_ass = canv.create_rectangle(self.x * self.world.size, self.y * self.world.size,
                                            (self.x + 1) * self.world.size, (self.y + 1) * self.world.size, fill = 'black', width = 0)
            self.right_ass = canv.create_rectangle(self.x * self.world.size, self.y * self.world.size,
                                            (self.x + 1) * self.world.size, (self.y + 1) * self.world.size, fill = 'black', width = 0)
            if self.ii:
                self.ass = canv.create_rectangle(self.x * self.world.size, self.y * self.world.size, (self.x + 1) * self.world.size, (self.y + 1) * self.world.size, fill = 'black', width = 0)
        self.show()
    
    def tank_update(self):
        if self.ii:
            self.calculate()
        if self.lifes < 1:
            self.destroy()
            return
        if self.turning_left:
            self.turn_left()
        if self.turning_right:
            self.turn_right()
        if self.moving:
            self.move()
        if self.fireing:
            self.fire()
        self.show()
        self.points += 1
        if (self.x == 1) or (self.y == 1) or (self.x == self.world.x - 2) or (self.y == self.world.y - 2):
            self.points -= 10
    
    def charging(self):
        self.charge_part += 1
    
    
    def calculate(self):
        movup = 0
        movleft = 0
        for i in self.world.tanks:
            if i != self:
                delta_x = self.x - i.x
                delta_y = self.y - i.y
                movup += self.w[0] * delta_y
                movleft += self.w[0] * delta_x
                movup += self.w[1] / (delta_y + 0.5)
                movleft += self.w[1] / (delta_x + 0.5)
                movup += self.w[2] / (delta_y + 0.5) ** 2
                movleft += self.w[2] / (delta_x + 0.5) ** 2
        if abs(movup) > abs(movleft):
            if movup > 50:
                if self.course == 'up':
                    self.turning_left = False
                    self.turning_right = False
                    self.moving = True
                if self.course == 'left':
                    self.turning_left = False
                    self.turning_right = True
                    self.moving = False
                if self.course == 'right':
                    self.turning_left = True
                    self.turning_right = False
                    self.moving = False
                if self.course == 'down':
                    self.turning_left = False
                    self.turning_right = False
                    if movleft > 0:
                        self.turning_right = True
                    else:
                        self.turning_left = True
                    self.moving = False
            elif movup < -50:
                if self.course == 'down':
                    self.turning_left = False
                    self.turning_right = False
                    self.moving = True
                if self.course == 'right':
                    self.turning_left = False
                    self.turning_right = True
                    self.moving = False
                if self.course == 'left':
                    self.turning_left = True
                    self.turning_right = False
                    self.moving = False
                if self.course == 'up':
                    self.turning_left = False
                    self.turning_right = False
                    if movleft > 0:
                        self.turning_left = True
                    else:
                        self.turning_right = True
                    self.moving = False
            else:
                self.turning_left = False
                self.turning_right = False
                self.moving = False
        else:  
            if movleft > 50:
                if self.course == 'left':
                    self.turning_left = False
                    self.turning_right = False
                    self.moving = True
                if self.course == 'down':
                    self.turning_left = False
                    self.turning_right = True
                    self.moving = False
                if self.course == 'up':
                    self.turning_left = True
                    self.turning_right = False
                    self.moving = False
                if self.course == 'right':
                    self.turning_left = False
                    self.turning_right = False
                    if movup > 0:
                        self.turning_left = True
                    else:
                        self.turning_right = True
                    self.moving = False
            elif movleft < -50:
                if self.course == 'right':
                    self.turning_left = False
                    self.turning_right = False
                    self.moving = True
                if self.course == 'up':
                    self.turning_left = False
                    self.turning_right = True
                    self.moving = False
                if self.course == 'down':
                    self.turning_left = True
                    self.turning_right = False
                    self.moving = False
                if self.course == 'left':
                    self.turning_left = False
                    self.turning_right = False
                    if movup > 0:
                        self.turning_right = True
                    else:
                        self.turning_left = True
                    self.moving = False
            else:
                self.turning_left = False
                self.turning_right = False
                self.moving = False
        fir = 0
        for i in self.world.tanks:
            if i != self:
                if self.course == 'up':
                    r = self.y - i.y
                if self.course == 'down':
                    r = 0 - self.y + i.y
                if self.course == 'left':
                    r = self.x - i.x
                if self.course == 'right':
                    r = 0 - self.x + i.x
                cos = r / (((self.x - i.x) ** 2 + (self.y - i.y) ** 2) ** 0.5 + 0.5)
                if cos != 0:
                    tan = (1 - cos ** 2) ** 0.5 / cos
                else:
                    tan = 1000
                fir += self.w[3] * r
                fir += self.w[4] * 1 / (r + 0.5)
                fir += self.w[5] * 1 / (r + 0.5) ** 2
                fir += self.w[6] * r * tan
                fir += self.w[7] * tan
                fir += self.w[8] * r * tan ** 2
        
        if fir > 0:
            self.fireing = True
        else:    
            self.fireing = False

    
    def destroy(self):
        if vision:
            canv.delete(self.centre)
            canv.delete(self.gun)
            canv.delete(self.left_bort)
            canv.delete(self.right_bort)
            canv.delete(self.left_ass)
            canv.delete(self.right_ass)
            if self.ii:
                canv.delete(self.ass)
        self.world.tanks.remove(self)
        self.world.dead_tanks.append(self)
    
    def show(self):
        if vision:
            lcol = 'black'
            if self.lifes == 3:
                lcol = 'green'
            if self.lifes == 2:
                lcol = 'yellow'
            if self.lifes == 1:
                lcol = 'red'
            ccol = 'black'
            if self.charges == 3:
                ccol = 'green'
            if self.charges == 2:
                ccol = 'yellow'
            if self.charges == 1:
                ccol = 'red'
            canv.itemconfig(self.centre, fill = lcol)
            canv.itemconfig(self.gun, fill = ccol)
            canv.coords(self.centre,self.x*self.world.size,self.y*self.world.size,(self.x+1)*self.world.size,(self.y+1)*self.world.size)
            if self.course == 'up':
                canv.coords(self.gun,self.x*self.world.size,(self.y-1)*self.world.size,(self.x+ 1) * self.world.size, self.y * self.world.size)
                canv.coords(self.left_bort,(self.x-1)*self.world.size,self.y*self.world.size,self.x*self.world.size,(self.y+1)*self.world.size)
                canv.coords(self.right_bort,(self.x+1)*self.world.size,self.y*self.world.size,(self.x+2)*self.world.size,(self.y+1)*self.world.size)
                canv.coords(self.left_ass,(self.x - 1)* self.world.size, (self.y + 1)* self.world.size, self.x * self.world.size, (self.y + 2) * self.world.size)
                canv.coords(self.right_ass,(self.x + 1)* self.world.size, (self.y + 1)* self.world.size, (self.x + 2) * self.world.size, (self.y + 2) *self.world.size)
                if self.ii:
                    canv.coords(self.ass,self.x * self.world.size, (self.y + 1)* self.world.size, (self.x + 1) * self.world.size, (self.y + 2) * self.world.size)
            if self.course == 'down':
                canv.coords(self.gun,self.x * self.world.size, (self.y + 1) * self.world.size, (self.x + 1) * self.world.size, (self.y  + 2)* self.world.size)
                canv.coords(self.right_bort,(self.x - 1)* self.world.size, self.y * self.world.size, self.x * self.world.size, (self.y + 1) * self.world.size)
                canv.coords(self.left_bort,(self.x + 1)* self.world.size, self.y * self.world.size, (self.x + 2) * self.world.size, (self.y + 1) * self.world.size)
                canv.coords(self.right_ass,(self.x - 1)* self.world.size, (self.y - 1)* self.world.size, self.x * self.world.size, self.y * self.world.size)
                canv.coords(self.left_ass,(self.x + 1)* self.world.size, (self.y - 1)* self.world.size, (self.x + 2) * self.world.size, self.y * self.world.size)
                if self.ii:
                    canv.coords(self.ass,self.x * self.world.size, (self.y - 1) * self.world.size, (self.x + 1) * self.world.size, self.y * self.world.size)
            if self.course == 'right':
                canv.coords(self.gun,(self.x + 1)* self.world.size, self.y * self.world.size, (self.x + 2) * self.world.size, (self.y + 1) * self.world.size)
                canv.coords(self.left_bort,self.x * self.world.size, (self.y - 1) * self.world.size, (self.x + 1) * self.world.size, self.y * self.world.size)
                canv.coords(self.right_bort,self.x * self.world.size, (self.y + 1)* self.world.size, (self.x + 1) * self.world.size, (self.y + 2) * self.world.size)
                canv.coords(self.left_ass,(self.x - 1)* self.world.size, (self.y - 1)* self.world.size, self.x * self.world.size, self.y * self.world.size)
                canv.coords(self.right_ass,(self.x - 1)* self.world.size, (self.y + 1)* self.world.size, self.x * self.world.size, (self.y + 2) * self.world.size)
                if self.ii:
                    canv.coords(self.ass,(self.x - 1)* self.world.size, self.y * self.world.size, self.x * self.world.size, (self.y + 1) * self.world.size)
            if self.course == 'left':
                canv.coords(self.gun,(self.x - 1)* self.world.size, self.y * self.world.size, self.x * self.world.size, (self.y + 1) * self.world.size)
                canv.coords(self.left_bort,self.x * self.world.size, (self.y + 1)* self.world.size, (self.x + 1) * self.world.size, (self.y + 2) * self.world.size)
                canv.coords(self.right_bort,self.x * self.world.size, (self.y - 1) * self.world.size, (self.x + 1) * self.world.size, self.y * self.world.size)
                canv.coords(self.left_ass,(self.x + 1)* self.world.size, (self.y + 1)* self.world.size, (self.x + 2) * self.world.size, (self.y + 2) * self.world.size)
                canv.coords(self.right_ass,(self.x + 1)* self.world.size, (self.y - 1)* self.world.size, (self.x + 2) * self.world.size, self.y * self.world.size)
                if self.ii:
                    canv.coords(self.ass,(self.x + 1)* self.world.size, self.y * self.world.size, (self.x + 2) * self.world.size, (self.y + 1) * self.world.size)
    
    def move(self):
        if (self.course == 'up') and (self.y != 1):
            self.points += 10
            self.y -= 1
        if (self.course == 'down') and (self.y != self.world.y - 2):
            self.points += 10
            self.y += 1
        if (self.course == 'right') and (self.x != self.world.x - 2):
            self.points += 10
            self.x += 1
        if (self.course == 'left') and (self.x != 1):
            self.points += 10
            self.x -= 1
    
    def turn_left(self):
        if self.course == 'up':
            self.course = 'left'
        elif self.course == 'left':
            self.course = 'down'
        elif self.course == 'down':
            self.course = 'right'
        elif self.course == 'right':
            self.course = 'up'
    
    def turn_right(self):
        if self.course == 'up':
            self.course = 'right'
        elif self.course == 'right':
            self.course = 'down'
        elif self.course == 'down':
            self.course = 'left'
        elif self.course == 'left':
            self.course = 'up'
    
    def start_turning_left(self, event):
        self.turning_left = True
    def start_turning_right(self, event):
        self.turning_right = True
    def end_turning_left(self, event):
        self.turning_left = False
    def end_turning_right(self, event):
        self.turning_right = False
        
    def start_moving(self, event):
        self.moving = True
    def end_moving(self, event):
        self.moving = False
        
    def start_fireing(self, event):
        self.fireing = True
    def end_fireing(self, event):
        self.fireing = False
    
    
    def fire(self):
        self.points -= 50
        if self.charges > 0:
            self.charges -= 1
            self.world.bullets.append(Bullet(self.world, self.x, self.y, self.course, self))
        
m = Map()
root.bind('<KeyPress-Escape>', exit)
"""
m.tanks.append(Tank(m, x = 1, course = 'right', ii = False))
root.bind('<KeyPress-Left>', m.tanks[0].start_turning_left)
root.bind('<KeyPress-Right>', m.tanks[0].start_turning_right)
root.bind('<KeyRelease-Left>', m.tanks[0].end_turning_left)
root.bind('<KeyRelease-Right>', m.tanks[0].end_turning_right)
root.bind('<KeyPress-Up>', m.tanks[0].start_moving)
root.bind('<KeyRelease-Up>', m.tanks[0].end_moving)
root.bind('<KeyPress-space>', m.tanks[0].start_fireing)
root.bind('<KeyRelease-space>', m.tanks[0].end_fireing)
"""
file = open('tanks_weights.csv', 'r')
weights = file.read().split('\n')
file.close()
m.spaun_bots()
m.update()
root.mainloop() 