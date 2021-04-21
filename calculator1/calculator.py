from tkinter import *
from PIL import ImageTk, Image

root = Tk()
# title of the project

root.title("Mathematical Calculator")
root.iconbitmap(r'calculator.ico')

e = Entry(root, width=15, borderwidth=15,bg='gray', font=('Times New Roman', 25))
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

button = ImageTk.PhotoImage(Image.open('circlr3.png'))
squ = ImageTk.PhotoImage(Image.open('squ.png'))
clear = ImageTk.PhotoImage(Image.open('clear.png'))
equal=ImageTk.PhotoImage(Image.open('equal.png'))


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global f_num
    global operator
    operator = "+"
    f_num = int(first_number)
    e.delete(0, END)


def button_sub():
    first_number = e.get()
    global f_num
    global operator
    operator = "-"
    f_num = int(first_number)
    e.delete(0, END)


def button_mul():
    first_number = e.get()
    global f_num
    global operator
    operator = "*"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global operator
    operator = "/"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    global operator
    second_number = e.get()
    e.delete(0, END)
    if operator == "+":
        e.insert(0, f_num + int(second_number))
    elif operator == "-":
        e.insert(0, f_num - int(second_number))
    elif operator == "*":
        e.insert(0, f_num * int(second_number))
    elif operator == "/":
        e.insert(0, f_num / int(second_number))


# defininnh the buttons
button_1 = Button(root, text="1", font=('Times New Roman', 20), image=button,width=0, compound=CENTER, padx=0, pady=0,
                  command=lambda: button_click(1), borderwidth=0)
button_2 = Button(root, text="2", font=('Times New Roman', 20), image=button, compound=CENTER, padx=0, pady=0,
                  command=lambda: button_click(2), borderwidth=0)
button_3 = Button(root, text="3", font=('Times New Roman', 20), image=button, compound=CENTER, padx=0, pady=0,
                  command=lambda: button_click(3), borderwidth=0)
button_4 = Button(root, text="4", font=('Times New Roman', 20), image=button, compound=CENTER, padx=0, pady=0,
                  command=lambda: button_click(4), borderwidth=0)
button_5 = Button(root, text="5", font=('Times New Roman', 20), image=button, compound=CENTER, padx=0, pady=0,
                  command=lambda: button_click(5), borderwidth=0)
button_6 = Button(root, text="6", font=('Times New Roman', 20), image=button, compound=CENTER, padx=0, pady=0,
                  command=lambda: button_click(6), borderwidth=0)
button_7 = Button(root, text="7", font=('Times New Roman', 20), image=button, compound=CENTER, padx=0, pady=0,
                  command=lambda: button_click(7), borderwidth=0)
button_8 = Button(root, text="8", font=('Times New Roman', 20), image=button, compound=CENTER, padx=0, pady=0,
                  command=lambda: button_click(8), borderwidth=0)
button_9 = Button(root, text="9", font=('Times New Roman', 20), image=button, compound=CENTER, padx=0, pady=0,
                  command=lambda: button_click(9), borderwidth=0)
button_0 = Button(root, text="0", font=('Times New Roman', 20), image=button, compound=CENTER, padx=0, pady=0,
                  command=lambda: button_click(0), borderwidth=0)
button_add = Button(root, text="+", font=('Times New Roman', 20,"bold"), image=squ, compound=CENTER, padx=0, pady=0,
                    command=button_add, borderwidth=0)
button_sub = Button(root, text="-", font=('Times New Roman', 20,"bold"), image=squ, compound=CENTER, padx=0, pady=0,
                    command=button_sub, borderwidth=0)
button_mul = Button(root, text="*", font=('Times New Roman', 20,"bold"), image=squ, compound=CENTER, padx=0, pady=0, command=button_mul, borderwidth=0)
button_div = Button(root, text="/", font=('Times New Roman', 20,"bold"), image=squ, compound=CENTER, padx=0, pady=0, command=button_div, borderwidth=0)
button_equal = Button(root, text="=", font=('Times New Roman', 20,"bold"), image=equal, compound=CENTER, padx=20, pady=0, command=button_equal, borderwidth=0)
button_clear = Button(root, text="Clear", font=('Times New Roman', 20), image=clear, compound=CENTER, padx=0, pady=0, command=button_clear, borderwidth=0)

# putting buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=1)
button_clear.grid(row=1, column=4)
button_add.grid(row=2, column=4)
button_sub.grid(row=3, column=4)
button_mul.grid(row=4, column=4)
button_div.grid(row=6, column=4)
button_equal.grid(row=6, column=0, columnspan=4)
root.mainloop()
