# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 왼쪽 파일을 오른쪽 파일로 변환하는 프로그램을 작성하라.
# 설계:
# - 원본 파일("input.txt")은 읽기 모드("r"), 결과 파일("output.txt")은 쓰기 모드("w")로 연다.
# - 원본 파일의 내용을 한 줄씩 읽어오며 반복문을 실행한다.
# - 읽어온 줄에 "line 2"가 포함되어 있다면 해당 줄을 쓰고 바로 아래에 "line 2-1"을 추가로 기록한다.
# - 그 외의 줄은 그대로 복사하여 기록한다.

infile = open("input.txt", "r")
outfile = open("output.txt", "w")

for line in infile:
  if "line 2" in line:
    outfile.write(line)
    outfile.write("line 2-1\n")
  else:
    outfile.write(line)

infile.close()
outfile.close()
