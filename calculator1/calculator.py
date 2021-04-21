from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Mathematical Calculator")
root.iconbitmap(r'calculator.ico')
root.title("Calculator")
label_result = Label(root, text="", width=17, borderwidth=10, bg='gray', font=('Times New Roman', 25))
label_result.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

button = ImageTk.PhotoImage(Image.open('circlr3.png'))
squ = ImageTk.PhotoImage(Image.open('squ.png'))
clear1 = ImageTk.PhotoImage(Image.open('clear.png'))
equal = ImageTk.PhotoImage(Image.open('equal.png'))
expression = ""


# creat functions
def add(value):
    global expression
    expression += value
    label_result.config(text=expression)


def clear():
    global expression
    expression = ""
    label_result.config(text=expression)


def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    label_result.config(text=result)


# creat GUI

button_1 = Button(root, text="1", font=('Times New Roman', 20), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: add("1"))
button_1.grid(row=1, column=0)

button_2 = Button(root, text="2", font=('Times New Roman', 20), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: add("2"))
button_2.grid(row=1, column=1)

button_3 = Button(root, text="3", font=('Times New Roman', 20), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: add("3"))
button_3.grid(row=1, column=2)

button_4 = Button(root, text="4", font=('Times New Roman', 20), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = Button(root, text="5", font=('Times New Roman', 20), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = Button(root, text="6", font=('Times New Roman', 20), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: add("6"))
button_6.grid(row=2, column=2)

button_7 = Button(root, text="7", font=('Times New Roman', 20), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: add("7"))
button_7.grid(row=3, column=0)

button_8 = Button(root, text="8", font=('Times New Roman', 20), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: add("8"))
button_8.grid(row=3, column=1)

button_9 = Button(root, text="9", font=('Times New Roman', 20), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: add("9"))
button_9.grid(row=3, column=2)

button_0 = Button(root, text="0", font=('Times New Roman', 20), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: add("0"))
button_0.grid(row=4, column=1)

button_divide = Button(root, text="/", font=('Times New Roman', 20), image=squ, compound=CENTER, borderwidth=0,
                       command=lambda: add("/"))
button_divide.grid(row=5, column=4)

button_multiply = Button(root, text="*", font=('Times New Roman', 20), image=squ, compound=CENTER, borderwidth=0,
                         command=lambda: add("*"))
button_multiply.grid(row=2, column=3, columnspan=2)

button_subtract = Button(root, text="-", font=('Times New Roman', 20), image=squ, compound=CENTER, borderwidth=0,
                         command=lambda: add("-"))
button_subtract.grid(row=3, column=3, columnspan=2)

button_clear = Button(root, text="Clear", font=('Times New Roman', 20), image=clear1, compound=CENTER, borderwidth=0,
                      command=lambda: clear())
button_clear.grid(row=1, column=4)

button_add = Button(root, text="+", font=('Times New Roman', 20), image=squ, compound=CENTER, borderwidth=0,
                    command=lambda: add("+"))
button_add.grid(row=4, column=3, columnspan=2)

button_equal = Button(root, text="=", font=('Times New Roman', 20), image=equal, compound=CENTER, borderwidth=0,
                      command=lambda: calculate())
button_equal.grid(row=5, column=0, columnspan=4)

root.mainloop()
