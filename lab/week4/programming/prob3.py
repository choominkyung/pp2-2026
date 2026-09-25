# 작성자: 추민경
# 작성일: 2026-09-25
# 문제: 상자를 나타내는 Box 클래스를 작성한다.
# 설계:
# - length, height, depth를 인스턴스 변수로 사용한다.
# - 생성자에서 세 값을 받는다.
# - 각 속성에 대한 getter와 setter를 작성한다.
# - 부피를 계산한다.


class Box:
    def __init__(self, length, height, depth):
        self.__length = length
        self.__height = height
        self.__depth = depth

    def __str__(self):
        return f"({self.__length}, {self.__height}, {self.__depth})"

    def setLength(self, length):
        self.__length = length

    def getLength(self):
        return self.__length

    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    def setDepth(self, depth):
        self.__depth = depth

    def getDepth(self):
        return self.__depth

    def getVolume(self):
        return self.__length * self.__height * self.__depth


def test_prob3():
    b1 = Box(100, 100, 100)

    print(b1)
    print("상자의 부피는", b1.getHeight() * b1.getLength() * b1.getDepth())


if __name__ == "__main__":
    test_prob3()