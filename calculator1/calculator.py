from tkinter import *

root = Tk()
# For title.
root.title("Mathematical Calculator")
root.iconbitmap(r'calculator.ico')

# Making text bar of the calculator.
cal_display = Label(root, text="", width=17, relief=SUNKEN, borderwidth=10, bg='gray', font=('Times New Roman', 25))
cal_display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Images used in the calculator button
button =PhotoImage(file='circlr3.png')
squ =PhotoImage(file='squ.png')
clear1 =PhotoImage(file='clear.png')
equal = PhotoImage(file='equal.png')

expression = ""

# Functiones in calculator.
def button_click(number):
    global expression
    expression += number
    cal_display.config(text=expression)


def clear():
    global expression
    expression = ""
    cal_display.config(text=expression)


def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "Enter correctly"
            expression = ""
    cal_display.config(text=result)


# creating buttons of calculator and its position.
button_1 = Button(root, text="1", font=('Times New Roman', 20,"bold"), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: button_click("1"))
button_1.grid(row=1, column=0)

button_2 = Button(root, text="2", font=('Times New Roman', 20,"bold"), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: button_click("2"))
button_2.grid(row=1, column=1)

button_3 = Button(root, text="3", font=('Times New Roman', 20,"bold"), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: button_click("3"))
button_3.grid(row=1, column=2)

button_4 = Button(root, text="4", font=('Times New Roman', 20,"bold"), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: button_click("4"))
button_4.grid(row=2, column=0)

button_5 = Button(root, text="5", font=('Times New Roman', 20,"bold"), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: button_click("5"))
button_5.grid(row=2, column=1)

button_6 = Button(root, text="6", font=('Times New Roman', 20,"bold"), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: button_click("6"))
button_6.grid(row=2, column=2)

button_7 = Button(root, text="7", font=('Times New Roman', 20,"bold"), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: button_click("7"))
button_7.grid(row=3, column=0)

button_8 = Button(root, text="8", font=('Times New Roman', 20,"bold"), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: button_click("8"))
button_8.grid(row=3, column=1)

button_9 = Button(root, text="9", font=('Times New Roman', 20,"bold"), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: button_click("9"))
button_9.grid(row=3, column=2)

button_0 = Button(root, text="0", font=('Times New Roman', 20,"bold"), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: button_click("0"))
button_0.grid(row=4, column=1)

button_dot = Button(root, text=".", font=('Times New Roman', 20,"bold"), image=button, compound=CENTER, borderwidth=0,
                  command=lambda: button_click("."))
button_dot.grid(row=4, column=2)

button_divide = Button(root, text="/", font=('Times New Roman', 20,"bold"), image=squ, compound=CENTER, borderwidth=0,
                       command=lambda: button_click("/"))
button_divide.grid(row=5, column=4)

button_multiply = Button(root, text="*", font=('Times New Roman', 20,"bold"), image=squ, compound=CENTER, borderwidth=0,
                         command=lambda: button_click("*"))
button_multiply.grid(row=2, column=3, columnspan=2)

button_subtract = Button(root, text="-", font=('Times New Roman', 20,"bold"), image=squ, compound=CENTER, borderwidth=0,
                         command=lambda: button_click("-"))
button_subtract.grid(row=3, column=3, columnspan=2)

button_clear = Button(root, text="Clear", font=('Times New Roman', 20,"bold"), image=clear1, compound=CENTER, borderwidth=0,
                      command=lambda: clear())
button_clear.grid(row=1, column=4)

button_add = Button(root, text="+", font=('Times New Roman', 20,"bold"), image=squ, compound=CENTER, borderwidth=0,
                    command=lambda: button_click("+"))
button_add.grid(row=4, column=3, columnspan=2)

button_equal = Button(root, text="=", font=('Times New Roman', 20,"bold"), image=equal, compound=CENTER, borderwidth=0,
                      command=lambda: calculate())
button_equal.grid(row=5, column=0, columnspan=4)

button_power = Button(root, text="^", font=('Times New Roman', 20,"bold"), image=button, compound=CENTER, borderwidth=0,
                    command=lambda: button_click("**"))
button_power.grid(row=4, column=0)

root.mainloop()
