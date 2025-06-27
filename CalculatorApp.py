from tkinter import *

# Creating a root widget (the main window)
root = Tk()
root.title("Calculator")
root.configure(bg="black")

# Creating an entry widget
e = Entry(root, width=30, font=('Arial', 24), fg="white", bg="black", borderwidth=5, justify='right')
e.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num, math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    try:
        second_number = float(e.get())
        e.delete(0, END)
        if math == "addition":
            e.insert(0, f_num + second_number)
        elif math == "subtraction":
            e.insert(0, f_num - second_number)
        elif math == "multiplication":
            e.insert(0, f_num * second_number)
        elif math == "division":
            if second_number == 0:
                e.insert(0, "Error")
            else:
                e.insert(0, f_num / second_number)
    except Exception:
        e.delete(0, END)
        e.insert(0, "Error")


def button_subtract():
    first_number = e.get()
    global f_num, math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num, math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num, math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


btn_params = {
    'padx': 20,
    'pady': 20,
    'font': ('Arial', 16),
    'bg': 'black',
    'fg': 'white',
    'activebackground': 'gray20',
    'activeforeground': 'white'
}


# Defining Buttons
button_0 = Button(root, text="0", command=lambda: button_click(0), **btn_params)
button_1 = Button(root, text="1", command=lambda: button_click(1), **btn_params)
button_2 = Button(root, text="2", command=lambda: button_click(2), **btn_params)
button_3 = Button(root, text="3", command=lambda: button_click(3), **btn_params)
button_4 = Button(root, text="4", command=lambda: button_click(4), **btn_params)
button_5 = Button(root, text="5", command=lambda: button_click(5), **btn_params)
button_6 = Button(root, text="6", command=lambda: button_click(6), **btn_params)
button_7 = Button(root, text="7", command=lambda: button_click(7), **btn_params)
button_8 = Button(root, text="8", command=lambda: button_click(8), **btn_params)
button_9 = Button(root, text="9", command=lambda: button_click(9), **btn_params)
button_add = Button(root, text="+", command=button_add, **btn_params)
button_equal = Button(root, text="=", command=button_equal, **btn_params)
button_clear = Button(root, text="Clear", command=button_clear, **btn_params)
button_subtract = Button(root, text="-", command=button_subtract, **btn_params)
button_multiply = Button(root, text="x", command=button_multiply, **btn_params)
button_divide = Button(root, text="/", command=button_divide, **btn_params)
button_decimal = Button(root, text=".", command=lambda: button_click('.'), **btn_params)




# Placing buttons in a neat grid
# Row 1 (Entry)
# Row 2
button_clear.grid(row=1, column=0, sticky="nsew")
button_divide.grid(row=1, column=1, sticky="nsew")
button_multiply.grid(row=1, column=2, sticky="nsew")
button_subtract.grid(row=1, column=3, sticky="nsew")
# Row 3
button_7.grid(row=2, column=0, sticky="nsew")
button_8.grid(row=2, column=1, sticky="nsew")
button_9.grid(row=2, column=2, sticky="nsew")
button_add.grid(row=2, column=3, sticky="nsew")
# Row 4
button_4.grid(row=3, column=0, sticky="nsew")
button_5.grid(row=3, column=1, sticky="nsew")
button_6.grid(row=3, column=2, sticky="nsew")
button_equal.grid(row=3, column=3, rowspan=2, sticky="nsew")
# Row 5
button_1.grid(row=4, column=0, sticky="nsew")
button_2.grid(row=4, column=1, sticky="nsew")
button_3.grid(row=4, column=2, sticky="nsew")
# Row 6
button_0.grid(row=5, column=0, columnspan=2, sticky="nsew")
button_decimal.grid(row=5, column=2, sticky="nsew")

# Make grid cells expand equally
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Running the main loop
root.mainloop()