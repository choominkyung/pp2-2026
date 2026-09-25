# 작성자: 추민경
# 작성일: 2026-09-25
# 문제: 삼각형을 나타내는 Triangle 클래스를 작성한다.
# 설계:
# - angle1, angle2, angle3을 인스턴스 변수로 사용한다.
# - numberOfSides는 삼각형의 변의 개수인 3으로 설정한다.
# - 각도에 대한 getter와 setter를 작성한다.
# - 세 각의 합이 180도인지 확인한다.


class Triangle:
    def __init__(self, a1, a2, a3):
        self.__angle1 = a1
        self.__angle2 = a2
        self.__angle3 = a3
        self.__numberOfSides = 3

    def __str__(self):
        return f"({self.__angle1}, {self.__angle2}, {self.__angle3})"

    def setAngle1(self, angle):
        self.__angle1 = angle

    def getAngle1(self):
        return self.__angle1

    def setAngle2(self, angle):
        self.__angle2 = angle

    def getAngle2(self):
        return self.__angle2

    def setAngle3(self, angle):
        self.__angle3 = angle

    def getAngle3(self):
        return self.__angle3

    def checkAngles(self):
        if self.__angle1 + self.__angle2 + self.__angle3 == 180:
            return True
        else:
            return False


def test_prob5():
    triangle = Triangle(90, 30, 60)

    print(triangle.checkAngles())


if __name__ == "__main__":
    test_prob5()