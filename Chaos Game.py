from random import randint
import turtle

turtle.screensize(2000, 2000)
wn = turtle.Screen()
wn.title("Chaos Game")
turtle.pencolor("red")
turtle.speed(0)


point_num = wn.numinput("Choosing Points", "How many corner points you would like to choose ?", 3, 3, 5)
if point_num == 3:
    side_len = wn.numinput("Lenght", "Side lenght of the Triangle (100-700): ", 200, 100, 700)
elif point_num == 4:
    side_len = wn.numinput("Lenght", "Side lenght of the Square (100-700): ", 200, 100, 700)
else:
    side_len = wn.numinput(
        "Lenght", "Side lenght of the Pentagon (100-700): ", 200, 100, 700)


def draw_corners(point_num, angle, side_len):
    count = 0
    corner_points = []
    while count <= point_num:
        turtle.forward(side_len)
        turtle.dot(8)
        corner_points.append(turtle.position())
        turtle.left(angle)
        count += 1
    # last point is also the first point so I have to remove it
    return corner_points[:-1]


if point_num == 3:
    turtle.penup()
    A, B, C = draw_corners(point_num, 120, side_len)
    Giv_Pon_x = wn.numinput(
        "Point", "X-coordinate of the point:", side_len // 2, 0, 1000)
    Giv_Pon_y = wn.numinput(
        "Point", "Y-coordinate of the point:", side_len // 2, 0, 1000)
    turtle.goto(Giv_Pon_x, Giv_Pon_y)
    pos = turtle.position()  # recording the position of the number
    turtle.dot(6, "blue")
    turtle.pencolor("black")
    for i in range(2000):
        die_num = randint(1, 6)
        if die_num == 1 or die_num == 2:
            new_pos_x = (pos[0] + A[0]) / 2
            new_pos_y = (pos[1] + A[1]) / 2
            turtle.goto(new_pos_x, new_pos_y)
            turtle.dot(5)
            pos = turtle.position()
        if die_num == 3 or die_num == 4:
            new_pos_x = (pos[0] + B[0]) / 2
            new_pos_y = (pos[1] + B[1]) / 2
            turtle.goto(new_pos_x, new_pos_y)
            turtle.dot(5)
            pos = turtle.position()
        if die_num == 5 or die_num == 6:
            new_pos_x = (pos[0] + C[0]) / 2
            new_pos_y = (pos[1] + C[1]) / 2
            turtle.goto(new_pos_x, new_pos_y)
            turtle.dot(5)
            pos = turtle.position()


if point_num == 4:
    turtle.penup()
    A, B, C, D = draw_corners(point_num, 90, side_len)
    Giv_Pon_x = wn.numinput(
        "Point", "X-coordinate of the point:", side_len // 2, 0, 1000)
    Giv_Pon_y = wn.numinput(
        "Point", "Y-coordinate of the point:", side_len // 2, 0, 1000)
    turtle.goto(Giv_Pon_x, Giv_Pon_y)
    pos = turtle.position()  # recording the position of the number
    turtle.dot(6, "blue")
    turtle.pencolor("black")
    g = 0
    w1 = [1, 2]
    w2 = [3, 4]
    w3 = [5, 6]
    w4 = [7, 8]
    for i in range(2000):
        w = randint(1, 8)
        if w in w1 and g not in w1:
            new_pos_x = (pos[0] + A[0]) / 2
            new_pos_y = (pos[1] + A[1]) / 2
            turtle.goto(new_pos_x, new_pos_y)
            turtle.dot(6)
            pos = turtle.position()
        if w in w2 and g not in w2:
            new_pos_x = (pos[0] + B[0]) / 2
            new_pos_y = (pos[1] + B[1]) / 2
            turtle.goto(new_pos_x, new_pos_y)
            turtle.dot(6)
            pos = turtle.position()
        if w in w3 and g not in w3:
            new_pos_x = (pos[0] + C[0]) / 2
            new_pos_y = (pos[1] + C[1]) / 2
            turtle.goto(new_pos_x, new_pos_y)
            turtle.dot(6)
            pos = turtle.position()
        if w in w4 and g not in w4:
            new_pos_x = (pos[0] + D[0]) / 2
            new_pos_y = (pos[1] + D[1]) / 2
            turtle.goto(new_pos_x, new_pos_y)
            turtle.dot(6)
            pos = turtle.position()
        g = w
 

if point_num == 5:
    turtle.penup()
    A, B, C, D, E = draw_corners(point_num, 72, side_len)

    Giv_Pon_x = wn.numinput("Point", "X-coordinate of the point:", int
                            (side_len//2), 0, 1000)
    Giv_Pon_y = wn.numinput("Point", "Y-coordinate of the point:", int
                            (side_len//2), 0, 1000)
    turtle.goto(Giv_Pon_x, Giv_Pon_y)
    pos = turtle.position()
    turtle.dot(6, "blue")
    turtle.pencolor("black")
    g = 0
    w1 = [1, 2]
    w2 = [3, 4]
    w3 = [5, 6]
    w4 = [7, 8]
    w5 = [9, 10]
    for i in range(5000):
        w = randint(1, 10)
        if w in w1 and g not in w1:
            new_pos_x = (pos[0] + A[0]) / 2
            new_pos_y = (pos[1] + A[1]) / 2
            turtle.goto(new_pos_x, new_pos_y)
            turtle.dot(6, "black")
            pos = turtle.position()
        if w in w2 and g not in w2:
            new_pos_x = (pos[0] + B[0]) / 2
            new_pos_y = (pos[1] + B[1]) / 2
            turtle.goto(new_pos_x, new_pos_y)
            turtle.dot(6, "black")
            pos = turtle.position()
        if w in w3 and g not in w3:
            new_pos_x = (pos[0] + C[0]) / 2
            new_pos_y = (pos[1] + C[1]) / 2
            turtle.goto(new_pos_x, new_pos_y)
            turtle.dot(6, "black")
            pos = turtle.position()
        if w in w4 and g not in w4:
            new_pos_x = (pos[0] + D[0]) / 2
            new_pos_y = (pos[1] + D[1]) / 2
            turtle.goto(new_pos_x, new_pos_y)
            turtle.dot(6, "black")
            pos = turtle.position()
        if w in w5 and g not in w5:
            new_pos_x = (pos[0] + E[0]) / 2
            new_pos_y = (pos[1] + E[1]) / 2
            turtle.goto(new_pos_x, new_pos_y)
            turtle.dot(6, "black")
            pos = turtle.position()
        g = w
