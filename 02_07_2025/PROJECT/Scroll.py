from tkinter import *
root = Tk()
root.title("Simple Scrollbar")
root.geometry("200x150")
frame = Frame(root)
frame.pack(pady=10)
scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(frame, yscrollcommand=scrollbar.set)
for i in range(1, 31):
    listbox.insert(END, f"Item {i}")
listbox.pack(side=LEFT)
scrollbar.config(command=listbox.yview)
root.mainloop()