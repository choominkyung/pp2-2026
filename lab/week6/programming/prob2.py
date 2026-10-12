# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 파일 "input.txt" 안에 저장된 단어 중에서 가장 긴 단어를 찾는 프로그램을 작성하라.
# 설계:
# - 파일을 읽기 모드로 열고 read()로 전체 텍스트를 읽어온다.
# - split()을 사용해 띄어쓰기 기준으로 단어들을 리스트로 쪼갠다.
# - 반복문으로 각 단어의 길이를 비교하여 가장 긴 단어를 찾고 출력한다.

file = open("input.txt", "r")
longest_word = ""

text = file.read()
words = text.split()

for word in words:
  if len(word) > len(longest_word):
    longest_word = word

print(f"가장 긴 단어는 {longest_word}입니다.")
file.close()
