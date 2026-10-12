# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 주사위를 나타내는 Dice 클래스를 상속받아 값이 3 이하이면 다시 던지는 FraudDice 클래스를 정의한다.
# 설계:
# - Dice 클래스의 roll() 메서드는 1~6 사이의 랜덤 숫자를 만든다.
# - FraudDice 클래스에서 roll() 메서드를 오버라이딩한다.
# - while 문을 사용하여 3 이하의 숫자가 나오면 4 이상이 나올 때까지 계속 주사위를 다시 굴리게 한다.

import random

class Dice:
    def __init__(self):
        self.value = 0

    # 주사위를 한 번 던져서 값을 저장하고 반환하는 메서드
    def roll(self):
        self.value = random.randint(1, 6)
        return self.value

class FraudDice(Dice):
    # 메서드 오버라이딩: 3 이하가 나오면 계속 다시 던지는 가짜 주사위 동작 구현
    def roll(self):
        while True:
            super().roll()  # 부모의 roll()을 불러와서 숫자를 뽑음
            if self.value > 3:  # 3보다 크면(즉 4, 5, 6이면) 멈춤
                break
        return self.value

# 객체 생성 및 테스트
normal_dice = Dice()
print("일반 주사위 결과:", normal_dice.roll())

fraud_dice = FraudDice()
print("사기 주사위 결과(3 초과만 나옴):", fraud_dice.roll())
