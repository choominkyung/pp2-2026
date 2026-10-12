# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 사용자로부터 파일 이름과 삭제할 문자열을 입력받아, 파일을 열어 해당 문자열을 삭제한 후에 다시 파일에 쓴다.
# 설계:
# - 파일 이름과 삭제할 문자열을 input으로 입력받는다.
# - 파일을 읽기 모드로 열어 전체 내용을 읽고, replace() 함수를 이용해 삭제할 문자열을 제거한다.
# - 쓰기 모드로 파일을 다시 열어 변경된 내용을 덮어쓴다.

filename = input("파일 이름을 입력하시오: ")
remove_str = input("삭제할 문자열을 입력하시오: ")

infile = open(filename, "r")
text = infile.read()
infile.close()

modified_text = text.replace(remove_str, "")

outfile = open("filename", "w")
outfile.write(modified_text)
outfile.close()
print("변경된 파일이 저장되었습니다.")
