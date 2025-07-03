from tkinter import *
master = Tk()
master.title("Horizontal Line on Canvas")
canvas_width = 200
canvas_height = 60
w = Canvas(master, width=canvas_width, height=canvas_height)
w.pack()
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y)
master.mainloop()