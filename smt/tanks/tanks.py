import tkinter as tk
import numpy as np
from random import randrange as rnd, choice
root = tk.Tk()
courses = ['up', 'down', 'right', 'left']
root.title("Box of tanks")
canv = tk.Canvas(root,bg='white')
canv.pack(fill=tk.BOTH,expand=1)

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
        for j in range(112):
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
        root.after(10, self.update)
    
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
                        b.parent.points += 1500
                    b.parent.points += 300
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
        self.id = canv.create_oval((self.x  + 0.1)* self.world.size, (self.y + 0.1)* self.world.size,
                                            (self.x + 0.9) * self.world.size, (self.y + 0.9) * self.world.size, fill = 'red', width = 0)
    
    def bullet_update(self):
        self.move()
        if (self.x < 0) or (self.y < 0) or (self.x > m.x - 1) or (self.y > m.y - 1):
            self.destroy()
        self.show()
    
    def show(self):
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
            self.ass = canv.create_rectangle(self.x * self.world.size, self.y * self.world.size,
                                            (self.x + 1) * self.world.size, (self.y + 1) * self.world.size, fill = 'black', width = 0)
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
    
    def charging(self):
        self.charge_part += 1
    
    
    def calculate(self):
        
        if self.course == 'up':
            mov = self.x * int(self.w[0]) + self.y * int(self.w[1]) + len(self.world.tanks) * int(self.w[2])
            for i in self.world.tanks:
                mov += (i.x - self.x) * self.w[12] + (i.y - self.y) * self.w[13]
                mov += 1 / (i.x - self.x + 0.5) * self.w[14] + 1 / (i.y - self.y + 0.5) * self.w[15]
        if self.course == 'down':
            mov = self.x * int(self.w[3]) + self.y * int(self.w[4]) + len(self.world.tanks) * int(self.w[5])
            for i in self.world.tanks:
                mov += (i.x - self.x) * self.w[16] + (i.y - self.y) * self.w[17]
                mov += 1 / (i.x - self.x + 0.5) * self.w[18] + 1 / (i.y - self.y + 0.5) * self.w[19]
        if self.course == 'right':
            mov = self.x * int(self.w[6]) + self.y * int(self.w[7]) + len(self.world.tanks) * int(self.w[8])
            for i in self.world.tanks:
                mov += (i.x - self.x) * self.w[20] + (i.y - self.y) * self.w[21]
                mov += 1 / (i.x - self.x + 0.5) * self.w[22] + 1 / (i.y - self.y + 0.5) * self.w[23]
        if self.course == 'left':
            mov = self.x * int(self.w[9]) + self.y * int(self.w[10]) + len(self.world.tanks) * int(self.w[11])
            for i in self.world.tanks:
                mov += (i.x - self.x) * self.w[24] + (i.y - self.y) * self.w[25]
                mov += 1 / (i.x - self.x + 0.5) * self.w[26] + 1 / (i.y - self.y + 0.5) * self.w[27]
        
        if self.course == 'up':
            turl = self.x * int(self.w[28]) + self.y * int(self.w[29]) + len(self.world.tanks) * int(self.w[30])
            for i in self.world.tanks:
                turl += (i.x - self.x) * self.w[31] + (i.y - self.y) * self.w[32]
                turl += 1 / (i.x - self.x + 0.5) * self.w[33] + 1 / (i.y - self.y + 0.5) * self.w[34]
        if self.course == 'down':
            turl = self.x * int(self.w[35]) + self.y * int(self.w[36]) + len(self.world.tanks) * int(self.w[37])
            for i in self.world.tanks:
                turl += (i.x - self.x) * self.w[38] + (i.y - self.y) * self.w[39]
                turl += 1 / (i.x - self.x + 0.5) * self.w[40] + 1 / (i.y - self.y + 0.5) * self.w[41]
        if self.course == 'right':
            turl = self.x * int(self.w[42]) + self.y * int(self.w[43]) + len(self.world.tanks) * int(self.w[44])
            for i in self.world.tanks:
                turl += (i.x - self.x) * self.w[45] + (i.y - self.y) * self.w[46]
                turl += 1 / (i.x - self.x + 0.5) * self.w[47] + 1 / (i.y - self.y + 0.5) * self.w[48]
        if self.course == 'left':
            turl = self.x * int(self.w[49]) + self.y * int(self.w[50]) + len(self.world.tanks) * int(self.w[51])
            for i in self.world.tanks:
                turl += (i.x - self.x) * self.w[52] + (i.y - self.y) * self.w[53]
                turl += 1 / (i.x - self.x + 0.5) * self.w[54] + 1 / (i.y - self.y + 0.5) * self.w[55]
        
        if self.course == 'up':
            turr = self.x * int(self.w[56]) + self.y * int(self.w[57]) + len(self.world.tanks) * int(self.w[58])
            for i in self.world.tanks:
                turr += (i.x - self.x) * self.w[59] + (i.y - self.y) * self.w[60]
                turr += 1 / (i.x - self.x + 0.5) * self.w[61] + 1 / (i.y - self.y + 0.5) * self.w[62]
        if self.course == 'down':
            turr = self.x * int(self.w[63]) + self.y * int(self.w[64]) + len(self.world.tanks) * int(self.w[65])
            for i in self.world.tanks:
                turr += (i.x - self.x) * self.w[66] + (i.y - self.y) * self.w[67]
                turr += 1 / (i.x - self.x + 0.5) * self.w[68] + 1 / (i.y - self.y + 0.5) * self.w[69]
        if self.course == 'right':
            turr = self.x * int(self.w[70]) + self.y * int(self.w[71]) + len(self.world.tanks) * int(self.w[72])
            for i in self.world.tanks:
                turr += (i.x - self.x) * self.w[73] + (i.y - self.y) * self.w[74]
                turr += 1 / (i.x - self.x + 0.5) * self.w[75] + 1 / (i.y - self.y + 0.5) * self.w[76]
        if self.course == 'left':
            turr = self.x * int(self.w[77]) + self.y * int(self.w[78]) + len(self.world.tanks) * int(self.w[79])
            for i in self.world.tanks:
                turr += (i.x - self.x) * self.w[80] + (i.y - self.y) * self.w[81]
                turr += 1 / (i.x - self.x + 0.5) * self.w[82] + 1 / (i.y - self.y + 0.5) * self.w[83]
        
        
        
        
        if self.course == 'up':
            fir = self.x * int(self.w[84]) + self.y * int(self.w[85]) + len(self.world.tanks) * int(self.w[86])
            for i in self.world.tanks:
                fir += (i.x - self.x) * self.w[87] + (i.y - self.y) * self.w[88]
                fir += 1 / (i.x - self.x + 0.5) * self.w[89] + 1 / (i.y - self.y + 0.5) * self.w[90]
        if self.course == 'down':
            fir = self.x * int(self.w[91]) + self.y * int(self.w[92]) + len(self.world.tanks) * int(self.w[93])
            for i in self.world.tanks:
                fir += (i.x - self.x) * self.w[94] + (i.y - self.y) * self.w[95]
                fir += 1 / (i.x - self.x + 0.5) * self.w[96] + 1 / (i.y - self.y + 0.5) * self.w[97]
        if self.course == 'right':
            fir = self.x * int(self.w[98]) + self.y * int(self.w[99]) + len(self.world.tanks) * int(self.w[100])
            for i in self.world.tanks:
                fir += (i.x - self.x) * self.w[101] + (i.y - self.y) * self.w[102]
                fir += 1 / (i.x - self.x + 0.5) * self.w[103] + 1 / (i.y - self.y + 0.5) * self.w[104]
        if self.course == 'left':
            fir = self.x * int(self.w[105]) + self.y * int(self.w[106]) + len(self.world.tanks) * int(self.w[107])
            for i in self.world.tanks:
                fir += (i.x - self.x) * self.w[108] + (i.y - self.y) * self.w[109]
                fir += 1 / (i.x - self.x + 0.5) * self.w[110] + 1 / (i.y - self.y + 0.5) * self.w[111]
        
        
        
        
        
        if mov > 0:
            self.moving = True
        else:    
            self.moving = False
        if turl > 0:
            self.turning_left = True
        else:    
            self.turning_left = False
        if turr > 0:
            self.turning_right = True
        else:    
            self.turning_right = False
        if fir > 0:
            self.fireing = True
        else:    
            self.fireing = False

    
    def destroy(self):
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
        self.points -= 58
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