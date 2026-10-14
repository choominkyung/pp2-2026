# 작성자: 추민경
# 작성일: 2026-10-14
# 문제: map()과 filter()를 사용하여서 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 중에서 짝수값의 제곱으로 새로운 리스트를 만드는 프로그램을 작성하라.
# 설계:
# - 주어진 리스트 데이터를 선언한다.
# - filter()를 사용하여 짝수만 골라낸 후, map()과 lambda를 사용하여 골라낸 짝수들의 제곱 값을 구한다.
# - 최종 결과를 리스트로 변환하여 출력한다.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(even_squares)