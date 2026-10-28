from tkinter import *

# 작성자: 추민경
# 작성일: 2026-10-28
# 문제: 배치 관리자를 이용하여 버튼을 3x10 격자 형태로 배치해보라.
# 설계:
# - Tkinter 창을 생성한다.
# - 2중 반복문을 사용하여 3행 10열의 버튼 객체를 생성한다.
# - 각 버튼의 텍스트를 "i행,j열"로 지정하고 grid() 메서드를 이용해 격자 형태로 배치한다.

window = Tk()
window.title("tk")

for i in range(3):
    for j in range(10):
        b = Button(window, text=f"{i}행,{j}열")
        b.grid(row=i, column=j)

window.mainloop()
