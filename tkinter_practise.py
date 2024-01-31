import tkinter as tk
from PIL import ImageTk, Image

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

root = tk.Tk()
root.title("Calculator")


img = Image.open("workflow.png")  # replace with your image file
img = img.resize((50, 50))  # resize image; adjust size as needed
img = ImageTk.PhotoImage(img)

# Create a label with the image
img_label = tk.Label(root, image=img)
img_label.grid(row=0, column=0, columnspan=4)  # place label in the first row

# Create the Entry field
entry = tk.Entry(root)
entry.grid(row=1, column=0, columnspan=4)

buttons = [
    ("1", 2, 0),
    ("2", 2, 1),
    ("3", 2, 2),
    ("4", 3, 0),
    ("5", 3, 1),
    ("6", 3, 2),
    ("7", 4, 0),
    ("8", 4, 1),
    ("9", 4, 2),
    ("0", 5, 0),
    ("+", 2, 3),
    ("-", 3, 3),
    ("*", 4, 3),
    ("/", 5, 3),
    ("=", 5, 2),
    ("C", 5, 1)
]

for button_text, row, column in buttons:
    button = tk.Button(root, text=button_text, padx=20, pady=10, command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column)

clear_button = tk.Button(root, text="Clear", padx=20, pady=10, command=button_clear)
clear_button.grid(row=6, column=0, columnspan=2)

equal_button = tk.Button(root, text="=", padx=20, pady=10, command=button_equal)
equal_button.grid(row=6, column=2, columnspan=2)

root.mainloop()
