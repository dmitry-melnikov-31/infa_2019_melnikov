from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import os
import sys


def update():
    if len(sys.argv) != 1:
        os.system("tanks.py " + sys.argv[1])
    else:
        os.system("tanks.py")
    root.after(2000, update)

    
root = tk.Tk()
update()
root.mainloop()