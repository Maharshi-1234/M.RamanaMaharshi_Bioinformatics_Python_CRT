from tkinter import *
root = Tk()
root.title("Simple Menu Without Function")
menubar = Menu(root)
root.config(menu=menubar)
menubar.add_command(label="Hello", command=lambda: print("Hello from Menu!"))
menubar.add_command(label="Exit", command=root.quit)
root.mainloop()