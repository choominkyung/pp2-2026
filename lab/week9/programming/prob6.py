 from tkinter import *
import random

# 작성자: 추민경
# 작성일: 2026-10-28
# 문제: 육면체 주사위 굴리기를 시뮬레이션하는 프로그램을 작성하라. "굴리기" 버튼이 하나 있어야 한다. 사용자가 버튼을 클릭하면 1부터 6 사이의 임의의 정수가 표시되어야 한다.
# 설계:
# - 주사위 눈을 표시할 Label 위젯과 "굴리기" Button 위젯을 생성한다.
# - 버튼 클릭 시 random.randint(1, 6)을 사용하여 1부터 6 사이의 난수를 발생시키고 레이블에 출력한다.

def roll_dice():
    dice_value = random.randint(1, 6)
    label.config(text=str(dice_value))

window = Tk()
window.title("Dice Roll")

label = Label(window, text="1", font=("Arial", 30))
label.pack(pady=10)

roll_btn = Button(window, text="굴리기", width=15, command=roll_dice)
roll_btn.pack(pady=10)

window.mainloop()
