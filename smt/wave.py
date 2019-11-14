import tkinter as tk
import pandas as pd
import numpy as np
from random import randrange as rnd, choice


data = pd.read_csv("train.csv")
root = tk.Tk()
print(data)
#canv = tk.Canvas(root,bg='white')
#canv.pack(fill=tk.BOTH,expand=1)

def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)
        
def update():
    root.after(30, update)

#update()
#root.mainloop()