#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    while (wall_is_above() == False):
        move_up()
    if (wall_is_on_the_left()):
        while (wall_is_on_the_right() == False):
            move_right()
    else:
        while (wall_is_on_the_left() == False):
            move_left()


if __name__ == '__main__':
    run_tasks()
