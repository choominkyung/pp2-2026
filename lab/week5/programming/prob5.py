# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: Animal 클래스를 상속받아 고양이를 나타내는 Cat 클래스를 정의하고, 3마리의 고양이를 생성한 뒤 가장 나이가 많은 고양이를 찾는 함수를 구현한다.
# 설계:
# - Animal 부모 클래스를 정의하고 공통 속성(name, age)을 초기화한다.
# - Cat 클래스에서 Animal을 상속받고 breed(품종) 속성을 추가한다.
# - 3마리의 고양이 객체를 만들고 리스트에 담은 뒤, max() 함수와 람다식을 이용해 가장 나이가 많은 고양이를 찾는다.

class Animal:
    def __init__(self, name, age):
        self.name = name  # 이름
        self.age = age    # 나이

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)  # 부모 클래스의 __init__ 호출
        self.breed = breed           # 품종 추가

    # 고양이 정보를 예쁘게 출력하기 위한 __str__ 메서드
    def __str__(self):
        return f"이름: {self.name}, 나이: {self.age}, 품종: {self.breed}"

# 가장 나이가 많은 고양이를 찾아주는 함수
def get_oldest_cat(*args):
    # max() 함수를 사용하되, 고양이의 나이(age)를 기준으로 가장 큰 값을 찾음
    oldest = max(args, key=lambda cat: cat.age)
    return oldest

# --- 객체 생성 및 실행 테스트 ---
cat1 = Cat("나비", 3, "코숏")
cat2 = Cat("야옹이", 7, "페르시안")
cat3 = Cat("루비", 5, "러시안블루")

oldest_cat = get_oldest_cat(cat1, cat2, cat3)
print(f"가장 나이가 많은 고양이는 {oldest_cat.age}살입니다.")
