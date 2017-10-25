import tkinter as tk

window = tk.Tk()
window.title('Listbox')
window.geometry('500x400')

var1 = tk.StringVar()
l = tk.Label(window, bg = 'yellow', width = 20, height = 3, textvariable = var1)
l.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(window, listvariable = var2)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end',item)
lb.insert(1,'first')
lb.delete(2)


def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)
    
b = tk.Button(window, text = 'print selection', width = 20, height = 3, command = print_selection)
b.pack()
lb.pack()

window.mainloop()
        
