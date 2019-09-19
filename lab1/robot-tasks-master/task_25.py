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
    
    
@task(delay = 0.05)
def task_2_2():
    move_down()
    solar()
    for i in range(4):
        move_right(4)
        solar()


if __name__ == '__main__':
    run_tasks()
