#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    z = 1
    j = 1
    i = 1
    jj = 1
    while (wall_is_on_the_right() == False):
        move_right()
        z = z + 1
    while (wall_is_on_the_left() == False):
        move_left()
    if ((i != j) and (jj != (z - ii + 1))):
        fill_cell()
    for i in range(z - 1):
        ii = i + 2
        move_right()
        if ((ii != jj) and (jj != (z - ii + 1))):
            fill_cell()
    while (wall_is_on_the_left() == False):
        move_left()
    for j in range(z - 1):
        jj = j + 2
        move_down()
        if ((i != j) and (jj != (z - ii + 1))):
            fill_cell()
        for i in range(z - 1):
            ii = i + 2
            move_right()
            if ((ii != jj) and (jj != (z - ii + 1))):
                fill_cell()
        while (wall_is_on_the_left() == False):
            move_left()
        


if __name__ == '__main__':
    run_tasks()
