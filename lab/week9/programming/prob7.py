
# 작성자: 추민경
# 작성일: 2026-10-28
# 문제: 인치를 센티미터로 변환하는 다음과 같은 프로그램을 작성해보자.
# 설계:
# - 인치를 입력받을 Entry 위젯과 결과를 출력할 Label, 그리고 "변환!" 버튼을 배치한다.
# - 변환 버튼을 누르면 입력값을 가져와 2.54를 곱한 뒤 센티미터 단위로 레이블에 표시한다.
from tkinter import *
def convert():
    inch = float(entry.get())
    cm = inch * 2.54
    result_label.config(text=f"{cm} 센티미터")

window = Tk()
window.title("Inch to CM")

Label(window, text="인치를 입력하시오:").grid(row=0, column=0, padx=5, pady=5, sticky=W)
entry = Entry(window, width=15)
entry.grid(row=0, column=1, padx=5, pady=5)

Label(window, text="변환결과").grid(row=1, column=0, padx=5, pady=5, sticky=W)
result_label = Label(window, text="0.0 센티미터", bg="lightgray", width=20)
result_label.grid(row=1, column=1, padx=5, pady=5)

convert_btn = Button(window, text="변환!", command=convert)
convert_btn.grid(row=2, column=0, columnspan=2, pady=10)

window.mainloop()
