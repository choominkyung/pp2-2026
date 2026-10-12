# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 트윗 메시지에서 특수 문자, URL, 해쉬태그, 이메일 주소, RT, CC 등을 삭제하고 사용자 메시지만을 추려낸다.
# 설계:
# - 정규식(re) 모듈을 불러온다.
# - 정규식 패턴을 이용해 RT, CC, URL, 해시태그(#...), 사용자 태그(@...) 등을 빈 문자열로 치환한다.
# - 정제된 결과 문자열을 깔끔하게 정리하여 출력한다.

import re

tweet = "Good Morning! RT @PythonUser I like Python #Python"

# 정규식을 이용해 RT, @태그, #해시태그, URL 등을 제거
cleaned = re.sub(r"(RT|CC|http\S+|@\S+|#\S+)", "", tweet)
# 불필요하게 남은 여분의 공백들을 하나로 정리
cleaned = " ".join(cleaned.split())

print(f"트윗 문자열: '{tweet}'")
print(f"정제된 문자열: '{cleaned}'")
