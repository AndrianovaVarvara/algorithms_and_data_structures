import graphics as gr

window = gr.GraphWin("Derevnay", 500, 500)
''' На голубом фоне красный дом. Слева дерево, справа клумба с цветами.
В небе солнце, птички, облака'''


def draw_fon():
    nebo = gr.Rectangle(gr.Point(0, 0), gr.Point(500, 500))
    nebo.setFill('lightskyblue')

    grass = gr.Rectangle(gr.Point(0, 350), gr.Point(500, 500))
    grass.setFill('lightgreen')

    nebo.draw(window)
    grass.draw(window)


def draw_sun():
    sunC = gr.Circle(gr.Point(400, 100), 70)
    sunC.setFill('orange')
    sunB = gr.Circle(gr.Point(400, 100), 50)
    sunB.setFill('gold')
    sunA = gr.Circle(gr.Point(400, 100), 30)
    sunA.setFill('yellow')

    sunC.draw(window)
    sunB.draw(window)
    sunA.draw(window)


def cloud1():
    cloud1_1 = gr.Circle(gr.Point(100, 50), 20)
    cloud1_1.setFill('snow')
    cloud1_1.setOutline('snow')
    cloud1_2 = gr.Circle(gr.Point(130, 50), 20)
    cloud1_2.setFill('snow')
    cloud1_2.setOutline('snow')
    cloud1_3 = gr.Circle(gr.Point(115, 70), 20)
    cloud1_3.setFill('snow')
    cloud1_3.setOutline('snow')
    cloud1_4 = gr.Circle(gr.Point(90, 70), 20)
    cloud1_4.setFill('snow')
    cloud1_4.setOutline('snow')
    cloud1_5 = gr.Circle(gr.Point(140, 70), 20)
    cloud1_5.setFill('snow')
    cloud1_5.setOutline('snow')

    cloud1_1.draw(window)
    cloud1_2.draw(window)
    cloud1_3.draw(window)
    cloud1_4.draw(window)
    cloud1_5.draw(window)


def cloud2():
    cloud2_1 = gr.Circle(gr.Point(200, 100), 20)
    cloud2_1.setFill('snow')
    cloud2_1.setOutline('snow')
    cloud2_2 = gr.Circle(gr.Point(235, 100), 20)
    cloud2_2.setFill('snow')
    cloud2_2.setOutline('snow')
    cloud2_3 = gr.Circle(gr.Point(270, 100), 20)
    cloud2_3.setFill('snow')
    cloud2_3.setOutline('snow')
    cloud2_4 = gr.Circle(gr.Point(305, 100), 20)
    cloud2_4.setFill('snow')
    cloud2_4.setOutline('snow')
    cloud2_5 = gr.Circle(gr.Point(217, 85), 20)
    cloud2_5.setFill('snow')
    cloud2_5.setOutline('snow')
    cloud2_6 = gr.Circle(gr.Point(252, 85), 20)
    cloud2_6.setFill('snow')
    cloud2_6.setOutline('snow')
    cloud2_7 = gr.Circle(gr.Point(287, 85), 20)
    cloud2_7.setFill('snow')
    cloud2_7.setOutline('snow')

    cloud2_1.draw(window)
    cloud2_2.draw(window)
    cloud2_3.draw(window)
    cloud2_4.draw(window)
    cloud2_5.draw(window)
    cloud2_6.draw(window)
    cloud2_7.draw(window)


def draw_birds():
    bird1_1 = gr.Line(gr.Point(50, 100), gr.Point(70, 110))
    bird1_2 = gr.Line(gr.Point(70, 110), gr.Point(90, 100))
    bird2_1 = gr.Line(gr.Point(100, 115), gr.Point(115, 130))
    bird2_2 = gr.Line(gr.Point(115, 130), gr.Point(130, 115))
    bird3_1 = gr.Line(gr.Point(150, 100), gr.Point(170, 115))
    bird3_2 = gr.Line(gr.Point(170, 115), gr.Point(190, 100))

    bird1_1.draw(window)
    bird1_2.draw(window)
    bird2_1.draw(window)
    bird2_2.draw(window)
    bird3_1.draw(window)
    bird3_2.draw(window)


def draw_house():
    walls = gr.Polygon(gr.Point(200, 300), gr.Point(400, 300), gr.Point(400, 450), gr.Point(200, 450))
    walls.setFill('firebrick')
    walls.setOutline('saddlebrown')
    walls.setWidth(2)
    big_window = gr.Rectangle(gr.Point(250, 325), gr.Point(350, 400))
    big_window.setFill('lightcyan')
    big_window.setOutline('saddlebrown')
    big_window.setWidth(2)
    reshetka1 = gr.Line(gr.Point(300, 325), gr.Point(300, 400))
    resetka2 = gr.Line(gr.Point(250, 350), gr.Point(350, 350))
    roof = gr.Polygon(gr.Point(185, 315), gr.Point(300, 150), gr.Point(415, 315))
    roof.setOutline('saddlebrown')
    roof.setWidth(2)
    roof.setFill('peru')
    small_window = gr.Circle(gr.Point(300, 250), 20)
    small_window.setOutline('saddlebrown')
    small_window.setWidth(2)
    small_window.setFill('lightcyan')

    walls.draw(window)
    roof.draw(window)
    big_window.draw(window)
    reshetka1.draw(window)
    resetka2.draw(window)
    small_window.draw(window)


def draw_tree():
    stvol = gr.Rectangle(gr.Point(50, 360), gr.Point(80, 460))
    stvol.setFill('brown')
    krona = gr.Oval(gr.Point(20, 380), gr.Point(110, 210))
    krona.setFill('green')

    stvol.draw(window)
    krona.draw(window)


def second_tree():
    stvol2 = gr.Rectangle(gr.Point(90, 330), gr.Point(120, 430))
    stvol2.setFill('brown')
    krona2 = gr.Oval(gr.Point(60, 350), gr.Point(150, 180))
    krona2.setFill('green')

    stvol2.draw(window)
    krona2.draw(window)


def nadpis():
    msg = gr.Text(gr.Point(250, 470), 'Варя - умница!')
    msg.setStyle('bold')
    msg.setSize(30)
    msg.setTextColor('purple')

    msg.draw(window)


def risuem_kartinku():
    draw_fon()
    draw_sun()
    cloud1()
    cloud2()
    draw_birds()
    draw_house()
    second_tree()
    draw_tree()
    nadpis()


risuem_kartinku()

window.getMouse()
window.close()
