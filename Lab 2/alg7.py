import turtle
import random

def draw_triangle(points, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(points[0][0], points[0][1])
    turtle.goto(points[1][0], points[1][1])
    turtle.goto(points[2][0], points[2][1])
    turtle.goto(points[0][0], points[0][1])
    turtle.end_fill()

def midpoint(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2)

def fractal_mountain(points, depth):
    if type(depth) != int:
        raise TypeError("Depth should be of type 'int'")
    if depth < 0:
        raise ValueError("Recursion depth cannot be less than 0")
    if depth == 0:
        draw_triangle(points, random_color())
    else:
        mid1 = midpoint(points[0], points[1])
        mid2 = midpoint(points[1], points[2])
        mid3 = midpoint(points[2], points[0])
        
        mid2 = (mid2[0], mid2[1] + random.randint(10, 30))  # Случайный подъем вершины
        
        fractal_mountain([points[0], mid1, mid3], depth - 1)
        fractal_mountain([points[1], mid1, mid2], depth - 1)
        fractal_mountain([points[2], mid2, mid3], depth - 1)

def random_color():
    return (random.random(), random.random(), random.random())

def main():
    turtle.speed(0)
    turtle.bgcolor("skyblue")
    turtle.penup()
    turtle.goto(-200, -150)
    turtle.pendown()

    points = [(-200, -150), (0, 200), (200, -150)]
    fractal_mountain(points, 5)

    turtle.hideturtle()
    turtle.done()

main()
