import tkinter 
from tkinter import ttk

window = tkinter.Tk()

item_list = ["python", "Java", "C++", "Kotlin", "C#", "PHP"]
selected=tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Python",value=1,variable=selected)
r2 = ttk.Radiobutton(window, text="Java",value=2,variable=selected )
r3 = ttk.Radiobutton(window, text="C++",value=3,variable=selected )
r4 = ttk.Radiobutton(window, text="Kotlin",value=4,variable=selected )
r5 = ttk.Radiobutton(window, text="C#",value=5,variable=selected )
r6 = ttk.Radiobutton(window, text="PHP",value=6,variable=selected )


r1.grid(column=0, row=1, ipadx = 42, ipady=5)
r2.grid(column=0, row=2, ipadx = 50, ipady=5)
r3.grid(column=0, row=3, ipadx = 50, ipady=5)
r4.grid(column=0, row=4, ipadx=46, ipady=5)
r5.grid(column=0, row=5, ipadx=54, ipady=5)
r6.grid(column=0, row=6, ipadx=50, ipady=5)

def reset():
    selected.set(None)

Reset_button = ttk.Button(window, text="Reset", command=reset)
Reset_button.grid(column=0, row=9, sticky=tkinter.E, padx=4, pady=4)
# r4.grid(window,column=0, row=3, ipadx=5,ipady=5)
# r5.grid(window,column=0, row=4, ipadx=5,ipady=5)
# r6.grid(window,column=0, row=5, ipadx=5,ipady=5)

window.mainloop()