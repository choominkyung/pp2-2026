from tkinter import *

# 작성자: 추민경
# 작성일: 2026-10-28
# 문제: 다음과 같이 2개의 버튼을 가지는 카운터를 작성해보자. "감소" 버튼을 누르면 값은 1만큼 감소한다. "증가" 버튼을 누르면 값은 1만큼 증가한다.
# 설계:
# - 카운터 값을 관리할 전역 변수(counter)를 설정한다.
# - 현재 값을 보여줄 Label 위젯과 "감소", "증가" 버튼을 생성한다.
# - 버튼 클릭 시 값이 증감하고 레이블에 반영되는 함수를 구현하여 연결한다.

counter = 0

def decrease():
    global counter
    counter -= 1
    label.config(text=str(counter))

def increase():
    global counter
    counter += 1
    label.config(text=str(counter))

window = Tk()
window.title("Counter")

label = Label(window, text=str(counter), font=("Arial", 30))
label.pack(pady=10)

btn_frame = Frame(window)
btn_frame.pack(pady=10)

decrease_btn = Button(btn_frame, text="감소", width=10, command=decrease)
decrease_btn.pack(side=LEFT, padx=5)

increase_btn = Button(btn_frame, text="증가", width=10, command=increase)
increase_btn.pack(side=LEFT, padx=5)

window.mainloop()
