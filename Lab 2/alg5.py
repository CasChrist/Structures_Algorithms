import turtle
import random

def tree(branchLen, t):
    t.pensize(max(branchLen / 10, 1))  # Установка толщины ветви, минимум 1

    if branchLen > 5:
        t.forward(branchLen)

        # Поворот и рекурсия для правой ветви
        t.right(random.randint(15, 45))
        tree(branchLen - random.randint(10, 20), t)

        # Поворот и рекурсия для левой ветви
        t.left(random.randint(15, 45))
        tree(branchLen - random.randint(10, 20), t)

        # Возврат на исходную позицию
        t.right(random.randint(15, 45))
        t.backward(branchLen)
    else:
        t.color("green")  # Цвет листьев
        t.forward(branchLen)
        t.backward(branchLen)
        t.color("brown")  # Возврат к коричневому для ветвей

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)  # Начальное направление
    t.up()
    t.backward(100)  # Поднимаем черепаху
    t.down()
    t.color("brown")  # Начальный цвет ветвей
    tree(75, t)
    myWin.exitonclick()

main()
