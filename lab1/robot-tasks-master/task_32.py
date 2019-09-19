#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    z = 0
    while (wall_is_on_the_right() == False):
        if (wall_is_above()):
            if (cell_is_filled()):
                z = z + 1
            else:
                fill_cell()
        else:
            while (wall_is_above() == False):
                move_up()
                if (cell_is_filled()):
                    z = z + 1
                else:
                    fill_cell()
            while (wall_is_beneath() == False):
                move_down()
        move_right()
    mov('ax', z)


if __name__ == '__main__':
    run_tasks()
