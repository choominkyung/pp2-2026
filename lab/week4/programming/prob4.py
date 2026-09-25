# 작성자: 추민경
# 작성일: 2026-09-25
# 문제: 사각형을 나타내는 Rectangle 클래스를 작성한다.
# 설계:
# - x, y는 사각형의 왼쪽 상단 좌표이다.
# - width, height는 사각형의 크기이다.
# - 각 속성의 getter와 setter를 작성한다.
# - getArea()로 넓이를 계산한다.
# - overlap()으로 두 사각형이 겹치는지 확인한다.


class Rectangle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def __str__(self):
        return f"Rectangle({self.__x}, {self.__y}, {self.__width}, {self.__height})"

    def setX(self, x):
        self.__x = x

    def getX(self):
        return self.__x

    def setY(self, y):
        self.__y = y

    def getY(self):
        return self.__y

    def setWidth(self, width):
        self.__width = width

    def getWidth(self):
        return self.__width

    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    def getArea(self):
        return self.__width * self.__height

    def overlap(self, r):
        if (self.__x < r.getX() + r.getWidth() and
                self.__x + self.__width > r.getX() and
                self.__y < r.getY() + r.getHeight() and
                self.__y + self.__height > r.getY()):

            return True

        return False


def test_prob4():
    r1 = Rectangle(0, 0, 100, 100)
    r2 = Rectangle(10, 10, 100, 100)

    if r1.overlap(r2):
        print("r1과 r2는 서로 겹칩니다.")
    else:
        print("r1과 r2는 서로 겹치지 않습니다.")


if __name__ == "__main__":
    test_prob4()