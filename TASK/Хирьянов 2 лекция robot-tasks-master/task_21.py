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

@task(delay=0.05)
def task_4_11():
    n = 1
    while n != 14:
        if n % 2 != 0:  # нечет направо
            move_down()
            for i in range(n):
                move_right()
                fill_cell()
            move_right()
            n += 1
        else:            # чет налево
            move_down()
            for i in range(n):
                fill_cell()
                move_left()
            n += 1
    move_down()
    move_left(n-1)

if __name__ == '__main__':
    run_tasks()
