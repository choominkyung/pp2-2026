# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 2차원 점을 나타내는 Point 클래스를 상속받아 3차원 점 Point3D 클래스를 정의한다.
# 설계:
# - Point 클래스를 먼저 정의하고 x, y 인스턴스 변수와 __str__을 구현한다.
# - Point3D 클래스에서 Point를 상속받고 z 인스턴스 변수를 추가한다.
# - super()를 사용하여 부모의 __init__을 호출한다.

class Point:
    # 생성자: x, y 좌표를 받아 초기화
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 문자열 변환 함수: 객체를 출력할 때 (x, y) 형태로 반환
    def __str__(self):
        return f"({self.x}, {self.y})"

class Point3D(Point):
    # 생성자: x, y는 부모에게 넘기고 z는 자식이 직접 초기화
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    # 문자열 변환 함수: (x, y, z) 형태로 반환하도록 오버라이딩
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

# 객체 생성 및 테스트
p1 = Point(1, 2)
print("2차원 점:", p1)

p2 = Point3D(1, 2, 3)
print("3차원 점:", p2)
