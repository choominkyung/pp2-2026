# 작성자: 추민경
# 작성일: 2026-09-25
# 문제: 터틀 그래픽에서 2개의 거북이를 생성하고 서로 다른 방향으로 움직인다.
# 설계:
# - turtle 모듈을 사용한다.
# - Turtle 객체를 2개 생성한다.
# - 각각 다른 방향으로 움직이도록 한다.
# - 반복문을 사용하여 선을 그린다.


import turtle


def move_turtle(t, direction):
    for i in range(5):
        t.forward(100)
        t.right(direction)


def test_prob9():
    screen = turtle.Screen()

    turtle1 = turtle.Turtle()
    turtle2 = turtle.Turtle()

    turtle1.penup()
    turtle1.goto(-200, 100)
    turtle1.pendown()

    turtle2.penup()
    turtle2.goto(-200, -100)
    turtle2.pendown()

    turtle1.setheading(0)
    turtle2.setheading(180)

    for i in range(5):
        turtle1.forward(100)
        turtle1.right(90)

        turtle2.forward(100)
        turtle2.left(90)

    screen.mainloop()


if __name__ == "__main__":
    test_prob9()