# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 파일에서 임의의 행을 읽는 Python 프로그램을 작성하시오.
# 설계:
# - 사용자로부터 파일 이름과 읽고 싶은 행 번호를 입력받는다.
# - readlines()로 파일의 모든 줄을 리스트로 불러온다.
# - 인덱스 번호(입력받은 행 번호 - 1)를 이용해 해당 줄의 텍스트를 가져와 출력한다.

filename = input("파일 이름을 입력하시오: ")
line_num = int(input("행 번호를 입력하시오: "))

file = open(filename, "r")
lines = file.readlines()
target_line = lines[line_num - 1].strip()

print(f"{line_num}번 행은 {target_line}입니다.")
file.close()
