# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 텍스트 파일을 열어서 각 줄의 앞에 번호를 매겨서 다시 파일에 쓰는 프로그램을 작성하라.
# 설계:
# - 원본 파일을 읽기 모드로 열어 모든 줄을 readlines()로 가져온다.
# - 출력 파일을 쓰기 모드로 연다.
# - enumerate()를 사용하여 각 줄마다 1부터 시작하는 번호를 붙여서 새로운 파일에 기록한다.

infile = open("input.txt", "r")
lines = infile.readlines()
infile.close()

outfile = open("output.txt", "w")
for i, line in enumerate(lines, 1):
  outfile.write(f"{i}: {line}")
outfile.close()
print("각 줄 앞에 번호가 매겨져 저장되었습니다.")
