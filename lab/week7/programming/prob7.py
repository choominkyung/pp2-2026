# 작성자: 추민경
# 작성일: 2026-10-14
# 문제: 이테레이터를 구현하는 MyEnumerate라는 클래스를 작성해보자. 튜플의 첫 번째 요소는 0으로 시작되는 인덱스이고 튜플의 두 번째 요소는 주어진 자료 구조의 현재 요소이다. 각 반복마다 튜플을 반환해야 한다.
# 설계:
# - __init__()에서 반복할 데이터와 인덱스 초기값(0)을 설정한다.
# - __iter__()에서 객체 자신을 반환한다.
# - __next__()에서 인덱스와 현재 요소를 튜플 형태로 반환하고, 인덱스를 증가시키며, 범위를 벗어나면 StopIteration 예외를 발생시킨다.

class MyEnumerate:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration

        t = (self.index, self.data[self.index])
        self.index += 1
        return t


for index, letter in MyEnumerate('abc'):
    print(f"{index} : {letter}")