from tkinter import *

# 작성자: 추민경
# 작성일: 2026-10-28
# 문제: 주소를 입력하는 다음과 같은 애플리케이션을 작성해보자. 아래와 최대한 유사하게 작성하라.
# 설계:
# - 이름, 주소, 도, 우편번호, 국가 항목을 나타내는 Label과 데이터를 입력받는 Entry 위젯을 grid()로 배치한다.
# - 하단에 'Clear'와 'Submit' 버튼을 나란히 배치하여 주소 입력 폼 화면을 완성한다.

window = Tk()
window.title("tk")

labels = ["이름:", "주소:", "도:", "우편번호:", "국가:"]

for i, text in enumerate(labels):
    lbl = Label(window, text=text)
    lbl.grid(row=i, column=0, sticky=E, padx=5, pady=2)
    ent = Entry(window, width=50)
    ent.grid(row=i, column=1, columnspan=4, sticky=W, padx=5, pady=2)

clear_btn = Button(window, text="Clear", width=10)
clear_btn.grid(row=5, column=3, padx=5, pady=10, sticky=E)

submit_btn = Button(window, text="Submit", width=10)
submit_btn.grid(row=5, column=4, padx=5, pady=10, sticky=W)

window.mainloop()
