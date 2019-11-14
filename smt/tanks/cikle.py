from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import os

def update():
    os.system("tanks.py")
    root.after(5000, update)

    
root = tk.Tk()
update()
root.mainloop()