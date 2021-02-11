import graphics as gr

SIZE_X = 400
SIZE_Y = 400

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
#  Начальное положение шарика
coords = gr.Point(200, 200)
#  Скорость (скорость есть вектор из плоскости)
velocity = gr.Point(1, -2)
# Симуляция материальной точки представляет собой непрерывный процесс пересчёта координат по заданным нами законам
# При моделировании обычного равномерного движения, закон пересчёта будет X k+1 = X k + V*t
# Давайте будем считать, что t равно 1. Тогда все моменты времени отличаются ровно на 1. В таком случае,
# чтобы получить значения координат в следующий момент времени, нужно к текущим координатам прибавить скорость.
def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)
    return new_point

# Чтоб убрать лишнее (предыдущие нарисованные шарики)
def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)

# Процесс отрисовки шарика
def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)

# 
while True:
    clear_window()

    draw_ball(coords)
    coords = add(coords, velocity)

    gr.time.sleep(0.02)
