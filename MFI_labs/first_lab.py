import turtle


def paint_figure(number_of_angles: int, length: int) -> None:
    for i in range(number_of_angles):
        turtle.forward(length)
        turtle.left(360 / number_of_angles)


def paint_circle(radius: int) -> None:
    turtle.forward(radius)
    turtle.left(90)
    turtle.pendown()
    for i in range(360):
        turtle.left(1)
        turtle.forward(360 / (2 * radius))


def ten_squares(length: int) -> None:
    for i in range(10):
        paint_figure(4, length)
        #turtle.back(10)
        turtle.penup()
        turtle.setpos(turtle.xcor() - 10, turtle.ycor() - 10)
        turtle.pendown()
        length += 20


def spider(number_n: int, length_step: int) -> None:
    for i in range(number_n):
        turtle.right(360 / number_n)
        turtle.forward(length_step)
        turtle.clone()
        turtle.left(180)
        turtle.forward(length_step)
        turtle.right(180)


def test(random_num_one: int, random_num_two: int) -> int:
    result = random_num_one + random_num_two
    return result


def circle_spiral() -> None:
    for i in range(300):
        turtle.forward(2 * i - 3/2 * i)
        turtle.left(32)


def squares_spiral() -> None:
    for i in range( 50, 800, 10):
        turtle.forward(i)
        turtle.left(90)


def task_9(length: int) -> None:
    a = 150
    turtle.left(a)
    for i in range(3, 8):
        paint_figure(i, length)
        length += 10
        turtle.penup()
        turtle.setpos(turtle.xcor() + 15, turtle.ycor())
        turtle.pendown()
        turtle.ontimer(None, 2000)
        turtle.setheading()
        turtle.left(90 + 180 / i)
        a -= 10


if __name__ == "__main__":
    turtle.circle(50)
    turtle.ontimer(None, 2020)
