# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 파일 "input.txt"의 처음 3줄을 읽는 프로그램을 작성하라.
# 설계:
# - open() 함수로 "input.txt"를 읽기 모드("r")로 연다.
# - for 문을 이용해 3번 반복하며 readline()으로 한 줄씩 읽어 출력한다.
# - 작업이 끝나면 close()로 파일을 닫는다.

file = open("lab/week6/programming/input.txt", "r")

for i in range(3):
  line = file.readline()
  print(line, end="")

file.close()
