from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['orange','yellow','green','blue']


def new_ball():
    global x,y,r,h,strike,counter
    if strike == False:
        print("miss")
    if counter == 10:
        canv.destroy()
        return
    counter += 1
    strike = False
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    h = 0.15
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    canv.create_oval(x-r*h,y-r,x+r*h,y-r*(1-2*h),fill = 'black', width=0)
    root.after(800,new_ball)

def click(event):
    rr = 3
    global score, strike, x, y, z, h, headshots, shots, lohs
    if strike == True:
        print("Not yet")
        return
    canv.create_oval(event.x-rr,event.y-rr,event.x+rr,event.y+rr,fill = 'black', width=0)
    strike = True
    if ((event.x - x) ** 2 + (event.y - (y - r + r * h)) ** 2) <= (r * h) ** 2:
        print("Headshot!")
        headshots += 1
        canv.create_oval(event.x-rr * 3,event.y-rr * 3,event.x+rr * 3,event.y+rr * 3,fill = 'red', width=0)
    elif ((event.x - x) ** 2 + (event.y - y) ** 2) <= r ** 2:
        shots += 1
        print("shot")
        canv.create_oval(event.x-rr,event.y-rr,event.x+rr,event.y+rr,fill = 'red', width=0)
    else:
        print("Loh")
        lohs += 1
        canv.create_oval(event.x-rr,event.y-rr,event.x+rr,event.y+rr,fill = 'black', width=0)
    return


headshots = 0
shots = 0
lohs = 0
counter = 0
score = 0        
strike = True        
print("\nStart\n")

def choic(event):
    print(event.x, event.y)
    return
new_ball()
canv.bind('<Button-1>', click)
mainloop()



score = headshots * 3 + shots - lohs
print('\n')
print("gg wp\n")
print("Your score:", score)
print("headshots:", (100 * headshots) // counter, "%")
print("shots:", (100 * shots) // counter, "%")
print("lohs:", (100 * lohs) // counter, "%")
print("\n  Your name: ", end = '')
name = input()
records = open("records.txt", 'r')
z = records.read()
records.close 
spis = z.split('\n')
records = open("records.txt", 'w')
dc = False
for i in range(len(spis) + 1):
    if dc == False:
        if int(spis[i].split(' ')[1]) > score:
            records.write(spis[i] + '\n')
        else:
            records.write(name + ' ' + str(score) + '\n')
            dc = True
    else:
        records.write(spis[i - 1] + '\n')    
records.close