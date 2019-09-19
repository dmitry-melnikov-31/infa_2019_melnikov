#!/usr/bin/python3

from pyrob.api import *


@task(delay = 0.05)
def task_8_28():
    if (wall_is_above() == False):
        move_up()
    while (wall_is_on_the_left() == False):
        move_left()
        if (wall_is_above() == False):
            move_up()
    while (wall_is_on_the_right() == False):
        move_right()
        if (wall_is_above() == False):
            move_up()
    while (wall_is_above() == False):
            move_up()
    while (wall_is_on_the_left() == False):
            move_left()





if __name__ == '__main__':
    run_tasks()
