from tkinter import *
root = Tk()
root.title("Simple Scale")
root.geometry("250x150")
label = Label(root, text="Scale Value: 0")
label.pack(pady=10)
def update(val):
    label.config(text=f"Scale Value: {val}")
scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=update)
scale.pack()
root.mainloop()
