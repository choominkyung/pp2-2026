# 작성자: 추민경
# 작성일: 2026-09-25
# 문제: 고양이를 나타내는 Cat 클래스를 작성한다.
# 설계:
# - Cat 클래스를 만든다.
# - name과 age를 인스턴스 변수로 사용한다.
# - 생성자, 문자열 변환 함수, getter/setter 함수를 작성한다.


class Cat:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return f"{self.__name} {self.__age}"

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age


def test_prob1():
    missy = Cat("Missy", 3)
    lucky = Cat("Lucky", 5)

    print(missy)
    print(lucky)


if __name__ == "__main__":
    test_prob1()