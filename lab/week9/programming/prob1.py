from tkinter import *

# 작성자: 추민경
# 작성일: 2026-10-28
# 문제: 다음과 같이 하나의 레이블과 하나의 버튼을 가지는 프로그램을 작성해보자. 버튼을 누르면 레이블은 'clicked'를 표시한다.
# 설계:
# - Tkinter 창을 생성하고 빈 텍스트를 가진 레이블과 'click me' 버튼을 배치한다.
# - 버튼을 클릭했을 때 호출되는 함수(click)를 정의하여 레이블의 텍스트를 "clicked"로 변경한다.

def click():
    label.config(text="clicked")

window = Tk()
window.title("Problem 01")

label = Label(window, text="")
label.pack()

button = Button(window, text="click me", command=click)
button.pack()

window.mainloop()
