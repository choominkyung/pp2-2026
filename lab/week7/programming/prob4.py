# 작성자: 추민경
# 작성일: 2026-10-14
# 문제: 람다식을 사용하여 정수 리스트를 필터링하는 프로그램을 작성하라.
# 설계:
# - 1부터 10까지의 정수가 담긴 리스트를 선언한다.
# - filter() 함수와 람다식을 사용하여 짝수와 홀수를 각각 필터링한다.
# - 원래 리스트와 필터링된 결과(짝수, 홀수)를 각각 출력한다.

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = list(filter(lambda x: x % 2 == 0, original_list))
odd_list = list(filter(lambda x: x % 2 != 0, original_list))

print(f"원래 리스트:\n{original_list}")
print(f"짝수:\n{even_list}")
print(f"홀수:\n{odd_list}")