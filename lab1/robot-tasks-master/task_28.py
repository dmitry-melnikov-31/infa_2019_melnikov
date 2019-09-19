#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    z = 0
    while (z != 5):
        if (cell_is_filled()):
            z = z + 1
        move_right()
    move_left()

if __name__ == '__main__':
    run_tasks()
