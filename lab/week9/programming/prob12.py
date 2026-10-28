from tkinter import *

# 작성자: 추민경
# 작성일: 2026-10-28
# 문제: 화면의 하단에 버튼을 4개 배치하고 이 버튼을 누르면 화면의 사각형이 상하좌우로 움직이는 애플리케이션을 작성해보자.
# 설계:
# - 캔버스에 사각형을 그리고 하단에 '<-(left)', '->(right)', '^(up)', 'V(down)' 버튼 4개를 배치한다.
# - 각 버튼 클릭 시 canvas.move()를 호출하여 사각형의 위치를 상하좌우로 이동시킨다.

def move_left():
    canvas.move(rect, -10, 0)

def move_right():
    canvas.move(rect, 10, 0)

def move_up():
    canvas.move(rect, 0, -10)

def move_down():
    canvas.move(rect, 0, 10)

window = Tk()
window.title("tk")

canvas = Canvas(window, width=500, height=350, bg="white")
canvas.pack()

rect = canvas.create_rectangle(200, 130, 300, 230, fill="tomato")

btn_frame = Frame(window)
btn_frame.pack(fill=X, pady=5)

btn_left = Button(btn_frame, text="<-(left)", command=move_left)
btn_left.pack(side=LEFT, expand=True, fill=X)

btn_right = Button(btn_frame, text="->(right)", command=move_right)
btn_right.pack(side=LEFT, expand=True, fill=X)

btn_up = Button(btn_frame, text="^(up)", command=move_up)
btn_up.pack(side=LEFT, expand=True, fill=X)

btn_down = Button(btn_frame, text="V(down)", command=move_down)
btn_down.pack(side=LEFT, expand=True, fill=X)

window.mainloop()
