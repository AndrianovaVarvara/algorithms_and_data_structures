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

@task
def task_5_4():
    n = 0
    while False == wall_is_beneath ():
        move_down()
        n += 1

    while True == wall_is_beneath():
        move_right()
        n += 1
    move_down()
    move_left()

    while True == wall_is_above () and False == wall_is_on_the_left():
        move_left()
        n += 1

if __name__ == '__main__':
    run_tasks()
