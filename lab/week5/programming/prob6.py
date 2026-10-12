# 작성자: 추민경
# 작성일: 2026-10-12
# 문제: 대학교의 학과(Department), 교과목(Course), 학생(Student) 간의 has-a 관계를 구현한다.
# 설계:
# - Department 클래스는 학과 이름과 개설된 교과목 리스트를 관리하고 교과목을 추가하는 add_course()를 가진다.
# - Course 클래스는 교과목 이름과 학점을 관리한다.
# - Student 클래스는 학생 이름과 학번을 관리하고 수강신청을 하는 enroll() 메서드를 가진다.

class Course:
    def __init__(self, name, credits):
        self.name = name          # 교과목 이름
        self.credits = credits    # 학점

class Department:
    def __init__(self, name):
        self.name = name          # 학과 이름
        self.courses = []         # 개설된 교과목들을 담을 리스트

    # 학과에 새로운 교과목을 생성해서 추가하는 메서드
    def add_course(self, name, credits):
        course = Course(name, credits)
        self.courses.append(course)
        return course

class Student:
    def __init__(self, name, student_id):
        self.name = name              # 학생 이름
        self.student_id = student_id  # 학번
        self.enrolled_courses = []    # 수강신청한 과목 리스트

    # 교과목을 수강신청하는 메서드
    def enroll(self, course):
        self.enrolled_courses.append(course)

# --- 객체 생성 및 실행 테스트 ---
dept = Department("컴퓨터")                               # 학과 생성
math1 = dept.add_course("공업수학", 3)                      # 교과목 1 추가
math2 = dept.add_course("이산수학", 2)                      # 교과목 2 추가

kim = Student("Kim", 20200001)                            # 학생 생성
kim.enroll(math1)                                         # 수강신청
print(f"학생 {kim.name}이 {kim.enrolled_courses[0].name}을 수강합니다.")
