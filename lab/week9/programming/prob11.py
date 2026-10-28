from tkinter import *
import time

# 작성자: 추민경
# 작성일: 2026-10-28
# 문제: 우리는 거리의 광고판에서 글자들이 수평으로 이동하는 애니메이션을 많이 본다. 파이썬을 이용하여 작성해보자.
# 설계:
# - 캔버스에 텍스트("파이썬 커피샵으로 오세요!")를 생성하고 무한 루프와 canvas.move()를 이용하여 수평 방향으로 이동시킨다.
# - 텍스트가 화면 끝을 벗어나면 다시 반대쪽으로 이동하도록 좌표를 처리한다.

window = Tk()
window.title("tk")

canvas = Canvas(window, width=500, height=300, bg="white")
canvas.pack()

text_id = canvas.create_text(50, 150, text="파이썬 커피샵으로 오세요!", font=("Arial", 16), anchor="w")

dx = 5

while True:
    canvas.move(text_id, dx, 0)
    coords = canvas.coords(text_id)
    
    # 화면 오른쪽 끝을 넘어가면 왼쪽 밖으로 위치 재설정
    if coords[0] > 500:
        canvas.coords(text_id, -200, 150)
        
    window.update()
    time.sleep(0.05)

window.mainloop()
