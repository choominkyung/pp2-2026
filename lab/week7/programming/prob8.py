
# 작성자: 추민경
# 작성일: 2026-10-14
# 문제: 호출될 때마다 앞의 수에 1을 더하여 반환하는 함수를 작성해보자. range()와 아주 유사하지만 이 함수는 상한값이 없다. 함수는 제너레이터를 이용하여 구현된다.
# 설계:
# - 제너레이터 함수를 정의하고, 시작 숫자를 매개변수로 받는다.
# - while True 무한 루프 안에서 yield를 사용하여 현재 숫자를 반환하고 숫자를 1씩 증가시킨다.

def my_range(start=0):
    current = start
    while True:
        yield current
        current += 1
for i in my_range(3):
    if i >= 8:
        break
    print(i)