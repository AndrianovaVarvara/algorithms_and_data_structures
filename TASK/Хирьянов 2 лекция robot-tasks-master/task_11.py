#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_4():
    while wall_is_on_the_right() == False:
        if wall_is_above() == True and wall_is_beneath() == True:
            fill_cell()
        move_right()

    if wall_is_on_the_right() == True:
        if wall_is_above() == True and wall_is_beneath() == True:
            fill_cell()


if __name__ == '__main__':
    run_tasks()
