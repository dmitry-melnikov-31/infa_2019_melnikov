#!/usr/bin/python3

from pyrob.api import *


@task(delay = 0.05)
def task_7_7():
    z = 0
    while ((wall_is_on_the_right() != True) and (z != 3)):
        if (cell_is_filled()):
            z = z + 1
        else:
            z = 0
        if (z != 3):
            move_right()


if __name__ == '__main__':
    run_tasks()
