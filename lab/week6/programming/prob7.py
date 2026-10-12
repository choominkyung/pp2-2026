# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 파일에서 데이터를 읽을 때, 파일이 없으면 IOError를 처리하여 다시 입력받는 프로그램을 작성하라.
# 설계:
# - 반복문(while True)을 사용하여 올바른 파일 이름이 입력될 때까지 입력을 받는다.
# - try 구문 안에서 open()을 시도하고, 성공하면 메시지를 출력한 뒤 반복을 탈출한다.
# - except IOError 발생 시 "파일이 없습니다. 다시 입력하시오."를 출력하고 계속 진행한다.

while True:
  filename = input("입력 파일 이름: ")
  try:
    infile = open(filename, "r")
    print(f"파일 {filename}이(가) 성공적으로 열렸습니다.")
    infile.close()
    break
  except IOError:
    print(f"파일 {filename}이(가) 없습니다. 다시 입력하시오.")
