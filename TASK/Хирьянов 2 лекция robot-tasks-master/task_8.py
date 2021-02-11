#!/usr/bin/python3

from pyrob.api import *

@task
def task_5_7():
    count = 0
    while wall_is_above() == True or wall_is_beneath() == True:
        if wall_is_above() == True and wall_is_beneath() == False:
            move_right()
        if wall_is_on_the_left() == True and wall_is_beneath() == True:
            move_right()
        if wall_is_beneath() == True and wall_is_on_the_left() == False:
            move_left()
            move_down()
            count += 1
            move_right()
        if wall_is_above() == False and count % 2 != 0:
            move_up()
            count += 1


if __name__ == '__main__':
    run_tasks()
