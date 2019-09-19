#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_4_3():
    move_up()
    for j in range(12):
        move_down()
        for i in range(27):
            move_right()
            fill_cell()
        move_left(27)
    move_right()
    move_down()


if __name__ == '__main__':
    run_tasks()
