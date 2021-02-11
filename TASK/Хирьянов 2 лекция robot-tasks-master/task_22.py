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

@task
def task_5_10():
    count= 0
    while cell_is_filled() == False:
        fill_cell()
        while wall_is_on_the_right() != True:
            move_right ()
            fill_cell()
        count += 1
        if wall_is_beneath() == False:
            move_down()
        fill_cell()
        while wall_is_on_the_left() != True:
            move_left()
            fill_cell()
        if wall_is_beneath() == False:
            move_down()
        count += 1
    if count%2 != 0:
        while wall_is_on_the_left() != True:
            move_left()

if __name__ == '__main__':
    run_tasks()
