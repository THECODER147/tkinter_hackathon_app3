import tkinter as tk

def addition():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"The result is: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

def subtraction():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 - num2
        result_label.config(text=f"The result is: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

def Multiply():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"The result is: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")

def Divide():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 / num2
        result_label.config(text=f"The result is: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers.")



Button_style = {
    "bg": "blue",
    "fg": "white",
    "activebackground": "green",
    "font": ("Times New Roman", 12, "bold"),
    "width": 12,
    "relief": "raised",
    "borderwidth": 2,
}


root = tk.Tk()
root.title("The Calculator")
root.geometry("800x850")
root.configure(bg = "red")

tk.Label(root, text="Number 1").grid()
entry1 = tk.Entry(root)
entry1.grid()

tk.Label(root, text="Number 2").grid()
entry2 = tk.Entry(root)
entry2.grid()

button_add = tk.Button(root, text="Add", command=addition, **Button_style)
button_add.grid(row=5, column=0)

button_sub = tk.Button(root, text="Substract", command=subtraction)
button_sub.grid(row=5, column=1)

button_mul = tk.Button(root, text="Multiply", command= Multiply)
button_mul.grid(row=5, column=2)

button_div = tk.Button(root, text="Divide", command=Divide)
button_div.grid(row=5, column=3)


result_label = tk.Label(root, text="The result is")
result_label.grid(row=20, column=5)
result_label

root.mainloop()
