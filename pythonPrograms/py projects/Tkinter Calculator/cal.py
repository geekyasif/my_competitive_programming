from tkinter import *
from tkinter.messagebox import *


def click_btn(event):
    btn = event.widget
    num = btn['text']
    text_field.insert(END, num)



root = Tk()

root.geometry("310x400")
root.title("Calculator")


text_field = Text(root, height=2, width=20, font=('Arial', 20))
text_field.grid(row=0,columnspan=5)


temp = 1
for i in range(1,4):
    for j in range(0,3):
        btn = Button(root, text=str(temp), width=3 ,relief="ridge", font=("Arial", 20))
        btn.grid(row=i, column=j, padx=5, pady=5)
        temp += 1
        btn.bind("<Button-1>", click_btn)


btn0 = Button(root, text="0", width=3 ,relief="ridge", font=("Arial", 20))
btn0.grid(row=4, column=0, padx=5, pady=5)
btn0.bind("<Button-1>", click_btn)

btnPoint = Button(root, text=".", width=3 ,relief="ridge", font=("Arial", 20))
btnPoint.grid(row=4, column=1)
btnPoint.bind("<Button-1>", click_btn)

btnEqual = Button(root, text="=", width=3 ,relief="ridge", font=("Arial", 20))
btnEqual.grid(row=4, column=2, padx=5, pady=5)
btnEqual.bind("<Button-1>", click_btn)

btnClear = Button(root, text="C", width=17 ,relief="ridge", font=("Arial", 20))
btnClear.grid(row=5, columnspan=5 ,padx=6, pady=5)
btnClear.bind("<Button-1>", click_btn)



# symbols

btnPlus = Button(root, text="+", width=3 ,relief="ridge", font=("Arial", 20))
btnPlus.grid(row=1, column=4 ,padx=8, pady=5)
btnPlus.bind("<Button-1>", click_btn)


btnMinus = Button(root, text="-", width=3 ,relief="ridge", font=("Arial", 20))
btnMinus.grid(row=2, column=4 ,padx=8, pady=5)
btnMinus.bind("<Button-1>", click_btn)


btnMul = Button(root, text="*", width=3 ,relief="ridge", font=("Arial", 20))
btnMul.grid(row=3, column=4 ,padx=8, pady=5)
btnMul.bind("<Button-1>", click_btn)


btnDiv = Button(root, text="/", width=3 ,relief="ridge", font=("Arial", 20))
btnDiv.grid(row=4, column=4 ,padx=8, pady=5)
btnDiv.bind("<Button-1>", click_btn)




root.mainloop()