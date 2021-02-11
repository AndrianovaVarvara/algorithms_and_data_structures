import graphics as gr
import math

'''Двигать веревку с шариком будем увеличивая-уменьшая угол. Двигаться будет и веревка и шар.
Если угол равен angle, то расстояние, на которое сдвинется шар по оси х будет равен sin_angel. 
При малых значениях angle sin_angle = angle (примерно до 20 градусов)
new_point_right = dlina + sin_angle (при движении вправо)
new_point_left = dlina - sin_angle (при движении влево)
Найдем расстояние, на которое сдвинется шар по оси у: 
new_point_right = dlina - (0.5 * (dlina ** 2 - new_point_right ** 2)
new_point_left = dlina - (0.5 * (dlina ** 2 - new_point_left ** 2)

Период колебаний Т - это промежуток времени, через который движение повторяется 
(т.е. шар возвращается в point_equilibrium). Вычисляется по формуле: T = 2 * pi * (0.5 * (dlina / g))
pi = 3.14, g = 9.8, dlina (переводим из пикселей в метры) = 0.079375, T = 0.18 

Четрые вектора движения: 
angle - увеличивается
angle - уменьшается.
'''
SIZE_X = 600
SIZE_Y = 600
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
# стартовые данные
point_base = gr.Point(300, 0)
point_equilibrium = gr.Point(300, 300)
dlina = 300
# рисуем шар на нитке
ball_null = gr.Circle(gr.Point(300, 300), 10)
line_null = gr.Line(gr.Point(300, 0), gr.Point(300, 300))
line_null.draw(window)
ball_null.draw(window)
ball_null.setFill('red')
# крайнее левое положение
sharik = gr.Circle(gr.Point(100, 223.6), 10)
verevka = gr.Line(gr.Point(300, 0), gr.Point(100, 223.6))
verevka.draw(window)
sharik.draw(window)
sharik.setFill('green')

for i in range(45):
    sharik.move

    gr.time.sleep(0.2)
# for i in range (45):
#     sharik.move(4.44, -1.697)
# for i in range(45):
#     sharik.move(-4.44, 1.697)
# for i in range(45):
#     sharik.move(-4.44, -1.697)
# for angle in range (20):
#     ball.move((dlina + math.sin(angle)), dlina - (0.5 * (dlina ** 2 - (dlina + math.sin(angle)) ** 2))


gr.time.sleep(0.2)
window.getMouse()
window.close()

    # point_left = gr.Point(100, 223.6)
    # point_right = gr.Point(500, 223.6)
    # volocity = gr.Point (4.44, 1.697)
    #
    # def add(point_1, point_2):
    #     new_point = gr.Point(point_1.x + point_2.x,
    #                          point_1.y + point_2.y)
    #     return new_point
    #
    # def update_points(point_equilibrium, volocity):
    #     return add(point_equilibrium, volocity)
    #
    # def check_points (point_equilibrium, volocity):
    #     if point_left.x == point_equilibrium.x:
    #         volocity.y = -volocity.y
    #     if point_equilibrium.x == point_right.x:
    #         volocity.x = -volocity.x
    #         volocity.y = -volocity.y
    #     if point_right.x == point_equilibrium.x:
    #         volocity.y = -volocity.y
    #     if point_equilibrium.x == point_left.x:
    #         volocity.x = -volocity.x
    #         volocity.y = -volocity.y
    #
    # def draw_ball():
    #     # # шарик в точке равновесия
    #     # circle = gr.Circle(gr.Point(300, 300), 10)
    #     # line = gr.Line(gr.Point(300, 0), gr.Point(300, 300))
    #     # line.draw(window)
    #     # circle.draw(window)
    #     # circle.setFill('red')
    #     # # крайнее правое положение
    #     # circle = gr.Circle(gr.Point(500, 223.6), 10)
    #     # line = gr.Line(gr.Point(300, 0), gr.Point(500, 223.6))
    #     # line.draw(window)
    #     # circle.draw(window)
    #     # circle.setFill('red')
    #     # # крайнее левое положение
    #     sharik = gr.Circle(gr.Point(100, 223.6), 10)
    #     verevka = gr.Line(gr.Point(300, 0), gr.Point(100, 223.6))
    #     verevka.draw(window)
    #     sharik.draw(window)
    #     sharik.setFill('green')
    #
    # sharik = gr.Circle(gr.Point(100, 223.6), 10)
    # verevka = gr.Line(gr.Point(300, 0), gr.Point(100, 223.6))
    # verevka.draw(window)
    # sharik.draw(window)
    # sharik.setFill('green')
    # verevka2 = gr.Line(gr.Point(300, 0), gr.Point(300, 300))
    # verevka2.draw(window)
    # circle = gr.Circle(gr.Point(300, 300), 10)
    # circle.draw(window)
    # circle.setFill('red')
    # circle3 = gr.Circle(gr.Point(500, 223.6), 10)
    # line3 = gr.Line(gr.Point(300, 0), gr.Point(500, 223.6))
    # line3.draw(window)
    # circle3.draw(window)
    # circle3.setFill('red')
    #
    #
    # for i in range(45):
    #     sharik.move (4.44, 1.697)
    # for i in range (45):
    #     sharik.move(4.44, -1.697)
    # for i in range(45):
    #     sharik.move(-4.44, 1.697)
    # for i in range(45):
    #     sharik.move(-4.44, -1.697)
