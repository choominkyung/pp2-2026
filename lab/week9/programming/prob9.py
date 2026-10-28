from tkinter import *

# 작성자: 추민경
# 작성일: 2026-10-28
# 문제: 데이터를 입력받을 때 사용할 수 있는 다음과 같은 애플리케이션을 작성해보자.
# 설계:
# - '이름', '직업', '국적' 항목을 나타내는 Label과 Entry 위젯을 grid로 배치한다.
# - 하단에 'Show'와 'Quit' 버튼을 배치하여 입력 정보를 확인하거나 프로그램을 종료하도록 구현한다.

def show_data():
    print(f"이름: {name_entry.get()}, 직업: {job_entry.get()}, 국적: {country_entry.get()}")

def quit_program():
    window.destroy()

window = Tk()
window.title("tk")

Label(window, text="이름").grid(row=0, column=0, sticky=W, padx=5, pady=5)
name_entry = Entry(window, width=25)
name_entry.grid(row=0, column=1, padx=5, pady=5)

Label(window, text="직업").grid(row=1, column=0, sticky=W, padx=5, pady=5)
job_entry = Entry(window, width=25)
job_entry.grid(row=1, column=1, padx=5, pady=5)

Label(window, text="국적").grid(row=2, column=0, sticky=W, padx=5, pady=5)
country_entry = Entry(window, width=25)
country_entry.grid(row=2, column=1, padx=5, pady=5)

btn_frame = Frame(window)
btn_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky=W)

show_btn = Button(btn_frame, text="Show", width=8, command=show_data)
show_btn.pack(side=LEFT, padx=2)

quit_btn = Button(btn_frame, text="Quit", width=8, command=quit_program)
quit_btn.pack(side=LEFT, padx=2)

window.mainloop()
