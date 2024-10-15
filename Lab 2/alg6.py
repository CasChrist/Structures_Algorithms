import turtle

def sierpinski_triangle(order, size):
    if order == 0:
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        # Рекурсивно рисуем 3 меньших треугольника
        sierpinski_triangle(order - 1, size / 2)
        turtle.forward(size / 2)
        sierpinski_triangle(order - 1, size / 2)
        turtle.backward(size / 2)
        turtle.left(60)
        turtle.forward(size / 2)
        turtle.right(60)
        sierpinski_triangle(order - 1, size / 2)
        turtle.left(60)
        turtle.backward(size / 2)
        turtle.right(60)

def main():
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-200, -150)
    turtle.pendown()
    sierpinski_triangle(4, 400)
    turtle.hideturtle()
    turtle.done()

main()
