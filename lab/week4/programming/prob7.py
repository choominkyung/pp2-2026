# 작성자: 추민경
# 작성일: 2026-09-25
# 문제: 사람들의 연락처를 저장하는 PhoneBook 클래스를 작성한다.
# 설계:
# - contacts라는 딕셔너리를 사용한다.
# - 이름을 key로 사용하고 연락처 정보를 value로 저장한다.
# - add() 함수로 연락처를 추가한다.
# - __str__()에서 저장된 연락처를 출력한다.


class PhoneBook:
    def __init__(self):
        self.__contacts = {}

    def __str__(self):
        result = ""

        for name, info in self.__contacts.items():
            result += name + "\n"
            result += "office phone: " + str(info["office"]) + "\n"
            result += "email address: " + str(info["email"]) + "\n\n"

        return result

    def add(self, name, mobile=None, office=None, email=None):
        self.__contacts[name] = {
            "mobile": mobile,
            "office": office,
            "email": email
        }


def test_prob7():
    obj = PhoneBook()

    obj.add("Kim", office="1234567", email="kim@company.com")
    obj.add("Park", office="2345678", email="park@company.com")

    print(obj)


if __name__ == "__main__":
    test_prob7()