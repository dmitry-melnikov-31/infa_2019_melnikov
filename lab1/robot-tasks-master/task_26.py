#!/usr/bin/python3

from pyrob.api import *

def solar():
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    move_up()
    move_left()
    fill_cell()
    move_up()
    
    
@task(delay=0.01)
def task_2_4():
    for i in range(4):
        solar()
        for j in range(9):
            move_right(4)
            solar()
        move_left(36)
        move_down(4)
    solar()
    for j in range(9):
        move_right(4)
        solar()
    move_left(36)

if __name__ == '__main__':
    run_tasks()
