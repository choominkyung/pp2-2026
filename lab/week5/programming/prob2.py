# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: Address와 Person 클래스를 다중 상속받아 연락처를 나타내는 Contact 클래스를 정의한다.
# 설계:
# - Address 클래스로 주소(street, city) 정보를 다룬다.
# - Person 클래스로 사람(name, email) 정보를 다룬다.
# - Contact 클래스에서 두 클래스를 동시에 상속받아(다중 상속) 연락처 정보를 완성한다.

class Address:
    def __init__(self, street, city):
        self.street = str(street)
        self.city = str(city)

class Person:
    def __init__(self, name, email):
        self.name = str(name)
        self.email = str(email)

class Contact(Address, Person):
    def __init__(self, name, email, street, city):
        # 다중 상속일 때는 각각의 부모 생성자를 직접 호출해 줌
        Address.__init__(self, street, city)
        Person.__init__(self, name, email)

    # 문자열 변환 함수: 연락처 정보를 한눈에 보기 쉽게 출력
    def __str__(self):
        return f"이름: {self.name}, 이메일: {self.email}, 주소: {self.city} {self.street}"

# 객체 생성 및 테스트
c = Contact("홍길동", "hong@example.com", "대학로 123", "서울시")
print(c)
