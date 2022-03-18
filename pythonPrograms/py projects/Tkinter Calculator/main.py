from tkinter import *
from tkinter.messagebox import *

calculation = ""
def cal(value):
    global calculation
    calculation += str(value)
    input.delete(1.0, "end")
    input.insert(1.0, calculation)

def calculate():
    global calculation
    try:
        calculation = str(eval(calculation))
        input.delete(1.0, "end")
        input.insert(1.0, calculation)
    except Exception as e:
        showerror('Error', e)


def clear():
    global calculation
    calculation = ""
    input.delete(1.0, 'end')


root = Tk()
root.geometry("295x330")
root.title("Calculator")

input = Text(root, height=2, width=16, font=("Arial", 24))
input.grid(columnspan=5)

btn1 = Button(root, text="1", width=3, command=lambda : cal(1), font=("Arial", 20))
btn1.grid(row=1, column=0)

btn2 = Button(root, text="2", width=3, command=lambda : cal(2), font=("Arial", 20))
btn2.grid(row=1, column=1)

btn3 = Button(root, text="3",  width=3, command=lambda : cal(3), font=("Arial", 20))
btn3.grid(row=1, column=2)


btn4 = Button(root, text="4", width=3,  command=lambda : cal(4), font=("Arial", 20))
btn4.grid(row=2, column=0)

btn5 = Button(root, text="5", width=3, command=lambda : cal(5), font=("Arial", 20))
btn5.grid(row=2, column=1)

btn6 = Button(root, text="6", width=3, command=lambda : cal(6), font=("Arial", 20))
btn6.grid(row=2, column=2)

btn7 = Button(root, text="7",  width=3, command=lambda : cal(7), font=("Arial", 20))
btn7.grid(row=3, column=0)

btn8 = Button(root, text="8", width=3,  command=lambda : cal(8), font=("Arial", 20))
btn8.grid(row=3, column=1)

btn9 = Button(root, text="9",  width=3, command=lambda : cal(9), font=("Arial", 20))
btn9.grid(row=3, column=2)

btn0 = Button(root, text="0", width=3,relief='ridge',  command=lambda : cal(0), font=("Arial", 20))
btn0.grid(row=4, column=1)

btnC = Button(root, text="C", width=3, relief='ridge',  command=clear, font=("Arial", 20))
btnC.grid(row=4, column=0)

btnEqual = Button(root, text="=", width=3, relief='ridge', command=calculate ,font=("Arial", 20))
btnEqual.grid(row=4, column=2)



# symbols ( -  +  *  / )

btnPlus = Button(root, text="+", width=3, relief='ridge', command=lambda : cal("+"), font=("Arial", 20))
btnPlus.grid(row=1, column=3)


btnMinus = Button(root, text="-",width=3, relief='ridge', command=lambda : cal("-"),  font=("Arial", 20))
btnMinus.grid(row=2, column=3)


btnMul = Button(root, text="*", width=3,  relief='ridge', command=lambda : cal("*"), font=("Arial", 20))
btnMul.grid(row=3, column=3)


btnDiv = Button(root, text="/", width=3, relief='ridge', command=lambda : cal("/"), font=("Arial", 20))
btnDiv.grid(row=4, column=3)

root.mainloop()
