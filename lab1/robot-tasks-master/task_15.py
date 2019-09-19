#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if (wall_is_above()):
        while (wall_is_beneath() == False):
            move_down()
    else:
        while (wall_is_above() == False):
            move_up()
    if (wall_is_on_the_right()):
        while (wall_is_on_the_left() == False):
            move_left()
    else:
        while (wall_is_on_the_right() == False):
            move_right()


if __name__ == '__main__':
    run_tasks()
