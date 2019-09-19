#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_4_11():
    move_down()
    for i in range(13):
        z = i + 1
        for j in range(z):
            move_right()
            fill_cell()
        move_left(i+1)
        move_down()
    move_right()

if __name__ == '__main__':
    run_tasks()
