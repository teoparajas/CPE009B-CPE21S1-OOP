from tkinter import *

class MyWindow:
    def __init__(self, win):
        win.configure(bg="Light Green")

        self.Label1 = Label(win, fg="Black", text="Calculator", font=("DS-Digital", 25, "bold"), bg="Light Green")
        self.Label1.grid(row=0, column=0, columnspan=4, pady=10, sticky=NSEW)

        self.Label2 = Label(win, text="Input Value 1:", font=("STENCIL", 15), bg="Light Green")
        self.Label2.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        self.Entry1 = Entry(win, bd=2, bg="Pink")
        self.Entry1.grid(row=1, column=2, columnspan=5, padx=10, pady=5, sticky=NSEW)

        self.Label3 = Label(win, text="Input Value 2:", font=("STENCIL", 15), bg="Light Green")
        self.Label3.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        self.Entry2 = Entry(win, bd=2, bg="Pink")
        self.Entry2.grid(row=2, column=2, columnspan=3, padx=10, pady=5, sticky=NSEW)

        self.Label4 = Label(win, text="Result:", font=("STENCIL", 15), bg="Light Green")
        self.Label4.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        self.Entry3 = Entry(win, bd=2, bg="Pink")
        self.Entry3.grid(row=3, column=3, columnspan=3, padx=10, pady=5, sticky=NSEW)

        self.Button1 = Button(win, fg="Red", text="Add")
        self.Button1.grid(row=4, column=0, padx=5, pady=10, sticky=NSEW)
        self.Button2 = Button(win, fg="Orange", text="Subtract")
        self.Button2.grid(row=4, column=1, padx=5, pady=10, sticky=NSEW)
        self.Button3 = Button(win, fg="Green", text="Multiply")
        self.Button3.grid(row=4, column=2, padx=5, pady=10, sticky=NSEW)
        self.Button4 = Button(win, fg="Blue", text="Divide")
        self.Button4.grid(row=4, column=3, padx=5, pady=10, sticky=NSEW)

        self.Button1.bind('<Button-1>', self.add)
        self.Button2.bind('<Button-1>', self.sub)
        self.Button3.bind('<Button-1>', self.multiply)
        self.Button4.bind('<Button-1>', self.divide)

        for i in range(5):
            win.grid_rowconfigure(i, weight=1)
        for j in range(4):
            win.grid_columnconfigure(j, weight=1)

    def add(self, event):
        self.calculate(lambda x, y: x + y)

    def sub(self, event):
        self.calculate(lambda x, y: x - y)

    def multiply(self, event):
        self.calculate(lambda x, y: x * y)

    def divide(self, event):
        self.calculate(lambda x, y: x / y)

    def calculate(self, operation):
        self.Entry3.delete(0, 'end')
        try:
            num1 = float(self.Entry1.get())
            num2 = float(self.Entry2.get())
            result = operation(num1, num2)

            if result.is_integer():
                self.Entry3.insert(END, str(int(result)))  # Convert to int for display
            else:
                self.Entry3.insert(END, str(result))  # Keep as float

        except ValueError:
            self.Entry3.insert(END, "Error: Invalid Input")
        except ZeroDivisionError:
            self.Entry3.insert(END, "Error: Division by Zero")

window = Tk()
MyWin = MyWindow(window)
window.geometry("500x400+10+10")
window.title("Simple Calculator")
window.mainloop()
