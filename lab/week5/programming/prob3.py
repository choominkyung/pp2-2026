# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 일반적인 함수 Function 클래스를 상속받아 2차 방정식을 나타내는 Quadratic 클래스를 정의한다.
# 설계:
# - Function 클래스에는 value() 메서드의 기틀을 만든다.
# - Quadratic 클래스에서 a, b, c 계수를 받고 value()를 오버라이딩하여 계산한다.
# - 2차 방정식의 근을 구하는 get_roots() 메서드를 추가한다.

import math

class Function:
    def value(self, x):
        pass

class Quadratic(Function):
    # 생성자: 2차 방정식의 계수 a, b, c를 인스턴스 변수로 저장
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # 메서드 오버라이딩: ax^2 + bx + c 값을 계산해서 반환
    def value(self, x):
        return self.a * (x ** 2) + self.b * x + self.c

    # 근의 공식을 이용해 2개의 실근을 계산해 반환하는 함수
    def get_roots(self):
        d = self.b ** 2 - 4 * self.a * self.c
        if d >= 0:
            r1 = (-self.b + math.sqrt(d)) / (2 * self.a)
            r2 = (-self.b - math.sqrt(d)) / (2 * self.a)
            return (r1, r2)
        else:
            return "실근이 없습니다."

# 객체 생성 및 테스트 (x^2 - 3x + 2 = 0)
q = Quadratic(1, -3, 2)
print("x=2 일 때 함수값:", q.value(2))
print("방정식의 해(근):", q.get_roots())
