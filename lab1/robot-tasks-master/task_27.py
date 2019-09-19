#!/usr/bin/python3

from pyrob.api import *


@task(delay = 0.05)
def task_7_5():
    move_right()
    fill_cell()
    move_left()
    z = 1
    x = 0
    while (wall_is_on_the_right() != True):
        move_right()
        if (wall_is_on_the_right() != True):
            if (z == x):
                fill_cell()
                z = z + 1
                x = 0
            x = x + 1


if __name__ == '__main__':
    run_tasks()
