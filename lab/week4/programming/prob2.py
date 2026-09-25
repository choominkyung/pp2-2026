# 작성자: 추민경
# 작성일: 2026-09-25
# 문제: 로켓을 나타내는 Rocket 클래스를 작성한다.
# 설계:
# - x, y를 로켓의 위치로 사용한다.
# - 생성자에서 x, y를 설정한다.
# - moveUp()을 호출하면 y좌표가 1 증가하도록 한다.


class Rocket:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"Rocket({self.__x}, {self.__y})"

    def moveUp(self):
        self.__y += 1

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y


def test_prob2():
    myRocket = Rocket()

    print("로켓의 높이:", myRocket.getY())

    myRocket.moveUp()

    print("로켓의 높이:", myRocket.getY())


if __name__ == "__main__":
    test_prob2()