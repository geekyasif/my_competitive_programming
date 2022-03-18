# list = []
# m = int(input("enter the size of list"))
# for i in range(0,m):
#     n = int(input("Enter number to store in list : "))
#     list.append(n)
#
# print(list)

# name = "Mohammad"
# number = 916180
# name = "asif"
# dict = {}
# for i in range(2):
#     dict.update()
# print(dict)
# list = []
# i=1
# j=1
# k=1
# n=2
# for i in range(i+1):
#     for j in range(j+1):
#         for k in range(k+1):
#             if i+j+k!=n:
#                 list.append([i,j,k])
# for i in list:
#     print(i)
# print([[a,b,c] for a in range(i+1) for b in range(j+1) for c in range(k+1) if a+b+c!=n])
# print([[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if x+y+z !=n])

# list = [["harry",37.21],["Berry",37.21],["Tina",37.2],["Akriti",41],["Harsh",39]]
# for i in list:
#     for j in i:
#         if j == i[1]:
#             temp = j
#             if j+1 < temp:
#                 print(temp)
# list = []
# n = 12
# for i in range(n):
#     list.insert

# arr = int(input("Enter the size of an array : "))
# for i in range(1,arr+1):
#     print(i)
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Pack a big frame so, it behaves like the window background
big_frame = ttk.Frame(root)
big_frame.pack(fill="both", expand=True)

# Just simply import the sun-valley.tcl file
widget.tk.call("source", "sun-valley.tcl")

# Then set the theme you want with the set_theme procedure
widget.tk.call("set_theme", "light")
# or
widget.tk.call("set_theme", "dark")

# Set the initial theme
root.tk.call("source", "sun-valley.tcl")
root.tk.call("set_theme", "light")


def change_theme():
    # NOTE: The theme's real name is sun-valley-<mode>
    if root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
    else:
        # Set dark theme
        root.tk.call("set_theme", "dark")

# Remember, you have to use ttk widgets
button = ttk.Button(big_frame, text="Change theme!", command=change_theme)
button.pack()

root.mainloop()
