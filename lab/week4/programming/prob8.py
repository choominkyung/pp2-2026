# 작성자: 추민경
# 작성일: 2026-09-25
# 문제: 노래 가사를 리스트로 저장하는 Song 클래스를 작성한다.
# 설계:
# - 노래 가사를 리스트로 저장한다.
# - sing() 메서드에서 리스트의 문자열을 한 줄씩 출력한다.


class Song:
    def __init__(self, lyrics):
        self.__lyrics = lyrics

    def sing(self):
        for line in self.__lyrics:
            print(line)


def test_prob8():
    lyrics = [
        "TWINKLE, twinkle, little star,",
        "How I wonder what you are!",
        "Up above the world so high,",
        "Like a diamond in the sky."
    ]

    aSong = Song(lyrics)
    aSong.sing()


if __name__ == "__main__":
    test_prob8()