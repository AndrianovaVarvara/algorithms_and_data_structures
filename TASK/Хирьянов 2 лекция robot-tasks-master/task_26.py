#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
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

    def perexod_R():
        for i in range(3):
            if wall_is_on_the_right() == False:
                move_right()

    def perexod_L():
        for i in range(3):
            if wall_is_on_the_left() == False:
                move_left()

    def stroka():
        for i in range(10):
            move_right()
            krest()
            perexod_R()
        move_down(4)
        for i in range(10):
            move_left()
            krest()
            perexod_L()
        move_down(4)


    # основная программа

    stroka()
    stroka()
    for i in range(10):
        move_right()
        krest()
        perexod_R()
    while wall_is_on_the_left() == False:
        move_left()


if __name__ == '__main__':
    run_tasks()
