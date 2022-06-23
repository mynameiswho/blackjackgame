from refactor_app import ApplicationWindow
import tkinter as tk

def hit():
    print('hey')
def stand():
    print('yo')

r = tk.Tk()
c = ApplicationWindow(r)
c.gui_setup(hit, stand)
c.grid(sticky='nsew')
r.mainloop()