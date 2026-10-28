from tkinter import *

# 작성자: 추민경
# 작성일: 2026-10-28
# 문제: 다음과 같이 하나의 레이블을 가지는 프로그램을 작성해보자. 레이블의 배경색은 오렌지색으로 하고, 글자색은 파랑색으로 한다. 레이블의 크기는 50x3으로 한다.
# 설계:
# - Tkinter 창을 생성한다.
# - Label 위젯의 배경색(bg)을 'orange', 글자색(fg)을 'blue', 크기를 width=50, height=3으로 설정한다.
# - 텍스트로 "Hello, I'm Label"을 입력하여 창에 배치한다.

window = Tk()
window.title("Welcome to tkinter")

label = Label(window, text="Hello, I'm Label", bg="orange", fg="blue", width=50, height=3)
label.pack()

window.mainloop()
