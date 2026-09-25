# 작성자: 추민경
# 작성일: 2026-09-25
# 문제: Person이라는 클래스를 작성한다.
# 설계:
# - name, mobile, office, email을 인스턴스 변수로 사용한다.
# - mobile, office, email은 기본값을 가진다.
# - 각 속성에 대한 getter와 setter 함수를 작성한다.


class Person:
    def __init__(self, n, m=None, o=None, e=None):
        self.__name = n
        self.__mobile = m
        self.__office = o
        self.__email = e

    def __str__(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setMobile(self, mobile):
        self.__mobile = mobile

    def getMobile(self):
        return self.__mobile

    def setOffice(self, office):
        self.__office = office

    def getOffice(self):
        return self.__office

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email


def test_prob6():
    p1 = Person("Kim", office="1234567", email="kim@company.com")

    p2 = Person("Park", office="2345678")

    p2.setEmail("park@company.com")


if __name__ == "__main__":
    test_prob6()