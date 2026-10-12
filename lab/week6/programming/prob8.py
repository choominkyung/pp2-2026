# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: scores.txt 파일에 저장된 부동소수점 성적을 읽어서 파일의 끝에 평균값을 추가하라.
# 설계:
# - 파일을 읽기 모드로 열어 모든 성적 데이터를 읽어온 후 각 줄의 값을 실수(float)로 변환하여 합계와 개수를 구한다.
# - 전체 평균을 계산한 뒤, 추가 모드("a")로 파일을 다시 열어 평균값을 기록한다.

infile = open("scores.txt", "r")
lines = infile.readlines()
infile.close()

total = 0.0
count = len(lines)

for line in lines:
  total += float(line.strip())

average = total / count if count > 0 else 0.0

outfile = open("scores.txt", "a")
outfile.write(f"평균값: {average:.1f}\n")
outfile.close()
print("성적 파일 끝에 평균값이 추가되었습니다.")
