import tkinter as tk

window = tk.Tk()
window.title('WordList')
window.geometry('500x500')

var = tk.StringVar()
var1 = tk.IntVar()
def Choose():
    global nc, wr, cr, nt, var, var1
    if var.get() == 'w':
        nc.config(state=tk.DISABLED)
        var1.set(0)
    else:
        nc.config(state=tk.NORMAL)
    if var1.get() == 0:
        nt.config(state=tk.DISABLED, background='grey')
    else:
        nt.config(state=tk.NORMAL, background='white')



title = tk.Label(window, text='Functions:').place(x=0, y=0, anchor='nw')
wr = tk.Radiobutton(window, text='Max length of words', variable=var, value='w', command=Choose)
wr.place(x=50, y=50, anchor='nw')
cr = tk.Radiobutton(window, text='Max length of letters', variable=var, value='c', command=Choose)
cr.place(x=50, y=100, anchor='nw')



# wt = tk.Text(window, height=1, borderwidth=5, width=10, state=tk.NORMAL).place(x=100, y=100, anchor='nw')
# ct = tk.Text(window, height=1, borderwidth=5, width=10, state=tk.NORMAL).place(x=100, y=150, anchor='nw')
nc = tk.Checkbutton(window, text='Assign length of words:', variable=var1, onvalue=1, offvalue=0, command=Choose)
nc.place(x=50, y=150, anchor='nw')
nt = tk.Text(window, height=1, borderwidth=5, width=10, state=tk.DISABLED, background='grey')
nt.place(x=100, y=200, anchor='nw')





window.mainloop()
