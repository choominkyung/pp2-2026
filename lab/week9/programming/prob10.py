from tkinter import *

# 작성자: 추민경
# 작성일: 2026-10-28
# 문제: 화면에 사각형을 그리고 마우스 왼쪽 버튼을 누르면 사각형의 크기를 증가시킨다. 마우스 오른쪽 버튼을 누르면 사각형이 작아지도록 하는 프로그램을 작성해보자.
# 설계:
# - 캔버스에 기본 사각형을 생성하고 좌클릭(<Button-1>) 시 크기를 늘리고, 우클릭(<Button-3>) 시 크기를 줄이는 이벤트 함수를 바인딩한다.

def increase_rect(event):
    global x1, y1, x2, y2
    x1 -= 5; y1 -= 5; x2 += 5; y2 += 5
    canvas.coords(rect, x1, y1, x2, y2)

def decrease_rect(event):
    global x1, y1, x2, y2
    x1 += 5; y1 += 5; x2 -= 5; y2 -= 5
    canvas.coords(rect, x1, y1, x2, y2)

window = Tk()
window.title("Rectangle Resize")

canvas = Canvas(window, width=400, height=300, bg="white")
canvas.pack()

x1, y1, x2, y2 = 150, 100, 250, 200
rect = canvas.create_rectangle(x1, y1, x2, y2)

canvas.bind("<Button-1>", increase_rect)
canvas.bind("<Button-3>", decrease_rect)

window.mainloop()
