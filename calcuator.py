#creating display of the window
import tkinter as tk

window = tk.Tk()
window.title("My Calculator")

# Creating buttons 
def clicked(number):  
    display.insert(tk.END, number)

def cb(number,row,column):
    button = tk.Button(
        window,
        text=number,command=lambda:clicked(number))
    button.grid(row=row,column=column)

#adding operations to it

def operation(op):
    global fn, operator
    
    fn = float(display.get())
    operator = op
    display.delete(0, tk.END)

plus_button = tk.Button(window, text="+",
                        command=lambda: operation("+"))
plus_button.grid(row=1, column=3)

minus_button = tk.Button(window, text="-",
                         command=lambda: operation("-"))
minus_button.grid(row=2, column=3)

multiply_button = tk.Button(window, text="*",
                            command=lambda: operation("*"))
multiply_button.grid(row=3, column=3)

divide_button = tk.Button(window, text="/",
                          command=lambda: operation("/"))
divide_button.grid(row=4, column=3)

clear_button = tk.Button(window, text="clear",
                        command=lambda:display.delete(0,tk.END))
clear_button.grid(row=5, column=3)

operator =""

def equals():
    global sn, operator
    
    sn = float(display.get())

    if operator == "+":
        result = fn + sn
    elif operator == "-":
        result = fn - sn
    elif operator == "*":
        result = fn * sn
    elif operator == "/":
        result = fn / sn

    display.delete(0, tk.END)
    display.insert(tk.END, result)

equals_button= tk.Button(window,text="=",command=equals)
equals_button.grid(row=2, column=3)

#creating calculator dislay
display = tk.Entry(window)
display.grid(row=0,column=0,columnspan=3)

cb(1,1,0)
cb(2,1,1)
cb(3,1,2)
cb(4,2,0)
cb(5,2,1)
cb(6,2,2)
cb(7,3,0)
cb(8,3,1)
cb(9,3,2)
cb(0,4,0)

window.mainloop()
#helps me keep running the window


# def seven():
#     print("You clicked 7!")
# command=seven
# button = tk.Button(window, text="7", command=seven)
# button.pack()

# def eight():
#     print("You clicked 8!")
# command=seven
# button = tk.Button(window, text="8", command=eight)
# button.pack() ##