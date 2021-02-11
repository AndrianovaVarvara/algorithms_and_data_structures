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
def task_8_30():
    # флаг_искать_проход := да
    # цикл пока флаг_искать_проход выполнять
    #     флаг_искать_проход := нет
    #     цикл пока справа_нет_стены выполнять
    #         шагнуть вправо
    #         цикл пока снизу_нет_стены выполнять
    #             шагнуть вниз
    #             флаг_искать_проход := да
    #         конец цикла
    #     конец цикла
    #     цикл пока слева_нет_стены выполнять
    #         шагнуть влево
    #         цикл пока снизу_нет_стены выполнять
    #             шагнуть вниз
    #             флаг_искать_проход := да
    #         конец цикла
    #     конец цикла
    # конец цикла
    def iskat_proxod ():

    while not iskat_proxod () :

        while not wall_is_on_the_right():
            move_right()
            while not wall_is_beneath():
                move_down()
                iskat_proxod == True
        while not wall_is_on_the_left():
            move_left()
            while not wall_is_beneath():
                move_down()
                iskat_proxod == True


if __name__ == '__main__':
    run_tasks()
