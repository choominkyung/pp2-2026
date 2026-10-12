# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 텍스트 파일을 열어서 파일 안의 스페이스 문자의 개수와 탭의 개수를 세는 프로그램을 작성하라.
# 설계:
# - 사용자로부터 파일 이름을 입력받아 읽기 모드로 연다.
# - read()로 파일 전체 내용을 읽어온 후, count() 메서드를 이용해 스페이스(' ')와 탭('\t')의 개수를 각각 센다.
# - 결과를 화면에 출력한다.

filename = input("파일 이름을 입력하시오: ")
infile = open(filename, "r")
text = infile.read()
infile.close()

space_count = text.count(" ")
tab_count = text.count("\t")

print(f"스페이스 수 = {space_count}, 탭의 수 = {tab_count}")
