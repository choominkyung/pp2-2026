import turtle


# BMI 계산
def bmi(height, weight):
    height = height / 100
    return weight / (height * height)


# BMI 결과
def bmi_result(value):
    if value < 18.5:
        return "저체중"
    elif value < 25:
        return "정상"
    elif value < 30:
        return "과체중"
    else:
        return "비만"


# health.txt 읽기
people = []

file = open("health.txt", "r", encoding="utf-8")

file.readline()

for line in file:
    data = line.split()

    phone = data[0]
    name = data[1]
    height = int(data[2])
    weight = int(data[3])

    value = bmi(height, weight)
    result = bmi_result(value)

    people.append([phone, name, height, weight, value, result])

file.close()


# 터틀 설정
t =turtle.Turtle()
# 표 그리기


# 표의 시작 위치
left = -400
top = 220

# 표의 크기
width = 660
height = 200

# 가로선
t.penup()
t.goto(-400, 220)
t.pendown()
t.goto(260, 220)
t.penup()
t.goto(-400, 180)
t.pendown()
t.goto(260, 180)
t.penup()
t.goto(-400, 140)
t.pendown()
t.goto(260, 140)
t.penup()
t.goto(-400, 100)
t.pendown()
t.goto(260, 100)
t.penup()
t.goto(-400, 60)
t.pendown()
t.goto(260, 60)
t.penup()
t.goto(-400, 20)
t.pendown()
t.goto(260, 20)

# 세로선
# 전화번호
t.penup()
t.goto(-400, 220)
t.pendown()
t.goto(-400, 20)

# 이름
t.penup()
t.goto(-200, 220)
t.pendown()
t.goto(-200, 20)

# 키
t.penup()
t.goto(-100, 220)
t.pendown()
t.goto(-100, 20)

# 몸무게
t.penup()
t.goto(-20, 220)
t.pendown()
t.goto(-20, 20)

# BMI
t.penup()
t.goto(80, 220)
t.pendown()
t.goto(80, 20)

# 소견 
t.penup()
t.goto(160, 220)
t.pendown()
t.goto(160, 20)

# 표 
t.penup()
t.goto(260, 220)
t.pendown()
t.goto(260, 20)



# 표안에 글자 넣기


t.penup()

t.goto(-390, 190)
t.write("전화번호")

t.goto(-190, 190)
t.write("이름")

t.goto(-90, 190)
t.write("키")

t.goto(-10, 190)
t.write("몸무게")

t.goto(90, 190)
t.write("BMI")

t.goto(170, 190)
t.write("소견")

#------------------------------

y = 150

for person in people:

    t.goto(-390, y)
    t.write(person[0])

    t.goto(-190, y)
    t.write(person[1])

    t.goto(-90, y)
    t.write(person[2])

    t.goto(-10, y)
    t.write(person[3])

    t.goto(90, y)
    t.write(f"{person[4]:.1f}")

    t.goto(170, y)
    t.write(person[5])

    y = y - 40


turtle.done()
