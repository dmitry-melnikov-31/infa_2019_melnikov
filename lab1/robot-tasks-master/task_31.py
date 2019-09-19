#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    vihod = 0
    while (vihod == 0):
        vihod = 1
        while ((wall_is_on_the_left() == False) and (wall_is_beneath())):
            move_left()        
        if (wall_is_beneath() == False):
            vihod = 0
            while (wall_is_beneath() == False):
                move_down()
            while (wall_is_on_the_right() == False):
                move_right()

if __name__ == '__main__':
    run_tasks()
