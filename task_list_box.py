import tkinter

window=tkinter.Tk()
lista = ['Python', 'C#', 'C++', 'Basic', 'Perl', 'Ruby', 'Java']
tk_list = tkinter.StringVar(value=lista)
listBox = tkinter.Listbox(window, height=10, listvariable=tk_list)
listBox.grid(column=0, row=1, sticky=tkinter.W)

label1 = tkinter.Label(text="Menu", bg="lightblue", fg="black")
label1.grid(column=0,row=0, padx=10, pady=10)

window.mainloop()