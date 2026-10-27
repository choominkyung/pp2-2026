# 작성자: 추민경
# 작성일: 2026-10-14
# 문제: 원을 나타내는 클래스 Circle에 +, >, < 연산자를 중복 정의해보자.
# 설계:
# - Circle 클래스의 생성자(__init__)를 정의하고 반지름(radius)을 속성으로 저장한다.
# - __add__ 메서드를 정의하여 두 원의 반지름을 더한 새로운 Circle 객체를 반환한다.
# - __gt__와 __lt__ 메서드를 정의하여 반지름 크기를 비교하도록 구현한다.

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def __add__(self, other):
        return Circle(self.__radius + other.__radius)

    def __gt__(self, other):
        return self.__radius > other.__radius

    def __lt__(self, other):
        return self.__radius < other.__radius

    def __str__(self):
        return f"Circle(radius={self.__radius})"
c1 = Circle(10)
c2 = Circle(20)

print(c1 + c2)
print(c1 > c2)
print(c1 < c2)
print(c1)
