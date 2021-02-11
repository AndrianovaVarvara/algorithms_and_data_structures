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
def task_8_21():
    if wall_is_above() == True and wall_is_on_the_right() == True:
        while wall_is_beneath() == False:
            move_left()
            move_down()
    elif wall_is_above() == True and wall_is_on_the_left() == True:
        while wall_is_beneath() == False:
            move_right()
            move_down()
    elif wall_is_beneath() == True and wall_is_on_the_left() == True:
        while wall_is_above() == False:
            move_right()
            move_up()
    else:
        while wall_is_above() == False:
            move_left()
            move_up()



if __name__ == '__main__':
    run_tasks()
