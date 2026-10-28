import tkinter as tk

root=tk.Tk()
root.title("Oobutton")
root.geometry("600X400")


def on_btn1_clicked():
    print("버튼1이 클릭되었습니다.")
label=tk.Label(root, text="객체지향원도우프로그래밍")
label.bind("Button-1>", on_label_clicked)
label.pack()

def on_btn1_clicked():
    print("버튼이 클릭되었습니다.")
    
btn1=tk.Button(root, text="클릭해볼까요?", command= on_btn1_clicked)
btn1.pack()


root.mainloop()
