import graphics as gr

SIZE_X = 400
SIZE_Y = 400

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

coords = gr.Point(200, 200)

velocity = gr.Point(1, -2)


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)

    return new_point


def clear_window():
    rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('green')
    rectangle.draw(window)


def draw_ball(coords):
    circle = gr.Circle(coords, 10)
    circle.setFill('red')

    circle.draw(window)

# упругое отражение шарика от стенок экрана. В теле основного цикла добавим функцию,
# которая будет проверять столкновение, и, в случае такого события, инвертировать скорость шарика по нужной оси.
def check_coords(coords, velocity):
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x

    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y


while True:
    clear_window()
    draw_ball(coords)
    coords = add(coords, velocity)
# добавляем в цикл новую переменную
    check_coords(coords, velocity)

    gr.time.sleep(0.02)