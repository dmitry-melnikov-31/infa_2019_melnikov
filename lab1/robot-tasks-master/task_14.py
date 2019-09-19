#!/usr/bin/python3

from pyrob.api import *


@task(delay = 0.05)
def task_8_11():
    while (wall_is_on_the_right() == False):
        if ((wall_is_above()) and (wall_is_beneath())):\
            fill_cell()
        if (wall_is_above() == False):
            move_up()
            fill_cell()
            move_down()
        if (wall_is_beneath() == False):
            move_down()
            fill_cell()
            move_up()
        move_right()
    if (wall_is_above() == False):
        move_up()
        fill_cell()
        move_down()
    if (wall_is_beneath() == False):
        move_down()
        fill_cell()
        move_up()
    if ((wall_is_above()) and (wall_is_beneath())):\
        fill_cell()


if __name__ == '__main__':
    run_tasks()
