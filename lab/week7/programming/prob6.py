# 작성자: 추민경
# 작성일: 2026-10-14
# 문제: 팩토리얼을 계산하는 함수 fact(n)을 작성하고 이것을 factorial이라는 모듈로 독립시켜 보자. 다른 파일에서 factorial 모듈을 포함시켜 안에 들어 있는 함수를 사용해보자.
# 설계:
# - (모듈 파일: factorial.py) 인수 n을 받아 반복문 또는 재귀를 통해 팩토리얼 값을 반환하는 fact(n) 함수를 정의한다.
# - (실행 파일: main.py) import factorial을 통해 모듈을 가져온 뒤 factorial.fact(5)와 같이 함수를 호출하여 결과를 확인한다.


def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


#--- 실행 파일에서 사용할 때 ---
#import factorial

#print(factorial.fact(5))