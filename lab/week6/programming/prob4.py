# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 현재 작업 디렉토리에 A.txt, B.txt, ..., z.txt 까지 총 26개의 텍스트 파일을 생성해보자.
# 설계:
# - string 모듈을 이용해 대문자 알파벳 문자열을 가져온다.
# - 반복문을 돌며 각 알파벳 뒤에 '.txt'를 붙여 파일 이름을 만든다.
# - 쓰기 모드("w")로 파일을 각각 열고 바로 닫아 26개의 빈 파일을 생성한다.

import string

for char in string.ascii_uppercase:
  filename = char + ".txt"
  file = open(filename, "w")
  file.close()

print("26개의 텍스트 파일이 생성되었습니다.")
