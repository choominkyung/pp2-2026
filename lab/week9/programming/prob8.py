from tkinter import *

# 작성자: 추민경
# 작성일: 2026-10-28
# 문제: 아이디와 패스워드를 입력할 수 있는 윈도우를 작성해보자. 아이디와 패스워드는 엔트리 위젯으로 구현된다. 격자 배치 관리자를 이용하여 배치된다. 버튼에 적절한 함수를 연결하여 버튼 이벤트를 처리한다.
# 설계:
# - grid 배치 관리자를 사용하여 아이디, 패스워드 레이블과 Entry 위젯을 배치한다 (비밀번호는 show='*' 설정).
# - 하단에 '로그인'과 '취소' 버튼을 배치하고 각각의 이벤트 함수를 연결한다.

def login():
    print(f"아이디: {id_entry.get()}, 패스워드: {pw_entry.get()}")

def cancel():
    id_entry.delete(0, END)
    pw_entry.delete(0, END)

window = Tk()
window.title("tk")

Label(window, text="아이디").grid(row=0, column=0, sticky=W, padx=5, pady=5)
id_entry = Entry(window, width=20)
id_entry.grid(row=0, column=1, padx=5, pady=5)

Label(window, text="패스워드").grid(row=1, column=0, sticky=W, padx=5, pady=5)
pw_entry = Entry(window, width=20, show="*")
pw_entry.grid(row=1, column=1, padx=5, pady=5)

btn_frame = Frame(window)
btn_frame.grid(row=2, column=0, columnspan=2, pady=5)

login_btn = Button(btn_frame, text="로그인", command=login)
login_btn.pack(side=LEFT, padx=2)

cancel_btn = Button(btn_frame, text="취소", command=cancel)
cancel_btn.pack(side=LEFT, padx=2)

window.mainloop()
