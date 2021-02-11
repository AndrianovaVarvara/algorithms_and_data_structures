#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    def krest():
        fill_cell()
        move_down()
        fill_cell()
        move_down()
        fill_cell()
        move_up()
        move_left()
        fill_cell()
        move_right(2)
        fill_cell()
        move_left()
        move_up()

    def perexod():
        for i in range  (4):
            if wall_is_on_the_right() == False:
                move_right()

    # основная программа
    move_right()
    move_down()
    for i in range (5):
        krest()
        perexod()

    move_left(2)




if __name__ == '__main__':
    run_tasks()
