import tkinter as tk
r = tk.Tk()
r.title("Vignan")
button = tk.Button(r, text='Enter',background="white",width=100,command=r.destroy)
button.pack()
button = tk.Button(r, text='Submit',background="red",width=100,command=r.destroy)
button.pack()
r.mainloop()