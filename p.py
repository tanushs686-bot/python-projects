import tkinter as tk

window = tk.Tk()

button1 = tk.Button(window, text="1")
button2 = tk.Button(window, text="2")
button3 = tk.Button(window, text="3")

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=0)

window.mainloop()