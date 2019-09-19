#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_27():
    while (cell_is_filled() == False):
        move_up()
    move_left()
    if (cell_is_filled() == False):
        move_right(2)


if __name__ == '__main__':
    run_tasks()
