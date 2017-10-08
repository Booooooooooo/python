import tkinter as tk

window = tk.Tk()
window.title('智障猪')
window.geometry('500x400')

t = tk.StringVar()
t.set("你猜呀")
play = False;
def zcx():
    global play
    if play == False:
        t.set("智障猪！")
        play = True
    else:
        t.set("你猜呀")
        play = False
    
b = tk.Button(window, text = 'zcx是？',width = 20, height = 5, command = zcx)
b.pack()
l = tk.Label(window, textvariable = t, width = 20, height = 5, bg = 'green', font = ('Arial',12))
l.pack()

window.mainloop()
        
