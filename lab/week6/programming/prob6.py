# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 현재의 작업 디렉토리에 "numbers.txt" 파일을 열어서 10개의 정수 난수를 문자열 형태로 추가하고 파일을 닫는 프로그램을 작성하라[span_12](start_span)[span_12](end_span)[span_13](start_span)[span_13](end_span).
# 설계:
# - 무작위 숫자를 뽑기 위해 random 모듈을 불러온다
import random

file = open("numbers.txt", "a")

for i in range(10):
  num = random.randint(1, 100)
  file.write(str(num) + "\n")

file.close()
print("10개의 정수 난수가 추가되었습니다.")
