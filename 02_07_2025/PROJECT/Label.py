from tkinter import *
root = Tk()
root.title("Label Example")
root.geometry("200x100")
label = Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)
root.mainloop()
