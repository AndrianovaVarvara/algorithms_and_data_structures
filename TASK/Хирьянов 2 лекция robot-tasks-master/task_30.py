#!/usr/bin/python3

from pyrob.api import *


# move_left(n=1)	Пройти n клеток влево (по умолчанию n = 1)
# move_right(n=1)	Пройти n клеток вправо (по умолчанию n = 1)
# move_up(n=1)	Пройти n клеток вверх (по умолчанию n = 1)
# move_down(n=1)	Пройти n клеток вниз (по умолчанию n = 1)
# wall_is_above()	если сверху стена, возвращает True, иначе — False
# wall_is_beneath()	если снизу стена, возвращает True, иначе — False
# wall_is_on_the_left()	если слева стена, возвращает True, иначе — False
# wall_is_on_the_right()	если справа стена, возвращает True, иначе — False
# fill_cell()	Закрасить текущую клетку
# cell_is_filled()	Возвращает True, если текущая клетка закрашена
# mov(r, v)	Поместить значение v в регистр r

@task(delay=0.01)
def task_9_3():
    def draw_cycle(side_length):
        i = 0
        while i < side_length - 1:
            if i > 0:
                fill_cell()
                move_up()
            else:
                move_up()
            i += 1
        i = 0
        while i < side_length - 1:
            if i > 0:
                fill_cell()
                move_right()
            else:
                move_right()
            i += 1
        i = 0
        while i < side_length - 1:
            if i > 0:
                fill_cell()
                move_down()
            else:
                move_down()
            i += 1
        i = 0
        while i < side_length - 1:
            if i > 0:
                fill_cell()
                move_left()
            else:
                move_left()
            i += 1


    side_length = 1
    while not wall_is_beneath():
        move_down()
        side_length += 1
    while side_length > 1:
        draw_cycle(side_length)
        move_right()
        move_up()
        side_length -= 2
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
