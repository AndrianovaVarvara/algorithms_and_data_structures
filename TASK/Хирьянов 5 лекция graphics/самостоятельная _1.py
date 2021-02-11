import graphics as gr
SIZE_X = 600
SIZE_Y = 600
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
circle = gr.Circle(gr.Point(200, 200), 10)
circle.draw(window)
circle.setFill('red')

coords = gr.Point(200, 200)
velocity = gr.Point(1,3)
acceleration = gr.Point(0,1)
def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point
def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)
    return new_point
def check_coords(coords, velocity):
    if coords.x < 0 or coords.x > SIZE_X:
        velocity.x = -velocity.x

    if coords.y < 0 or coords.y > SIZE_Y:
        velocity.y = -velocity.y
def update_coords(coords, velocity):
    return add(coords, velocity)
def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)
def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)
    G = 2000

    return gr.Point(-diff.x*G/distance_2, -diff.y*G/distance_2)
sun = gr.Circle(gr.Point(300, 300), 20)
sun.setFill('yellow')
sun.draw(window)
while True:
    circle.move
    acceleration = update_acceleration(coords, gr.Point(300, 300))
    coords = update_coords(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)

    gr.time.sleep(0.1)


window.getMouse()
window.close()
