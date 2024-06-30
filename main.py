import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculator")
root.geometry("450x650")
root.configure(bg="black")

display = tk.Entry(root, font=('Arial', 28), borderwidth=0, relief="solid", bg="black", fg="white")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

def button_click(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

def clear_display():
    display.delete(0, tk.END)

def create_round_button(canvas, text, row, column, command, bg, fg):
    btn_size = 90
    x0, y0, x1, y1 = 5, 5, btn_size - 5, btn_size - 5
    canvas.create_oval(x0, y0, x1, y1, fill=bg, outline=bg)

    btn = tk.Button(root, text=text, font=('Arial', 20), borderwidth=0, bg=bg, fg=fg, command=command)
    btn_window = canvas.create_window((btn_size // 2, btn_size // 2), window=btn)

    canvas.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')

buttons = [
    ('7', 1, 0, '#505050'), ('8', 1, 1, '#505050'), ('9', 1, 2, '#505050'), ('/', 1, 3, '#FF9500'),
    ('4', 2, 0, '#505050'), ('5', 2, 1, '#505050'), ('6', 2, 2, '#505050'), ('*', 2, 3, '#FF9500'),
    ('1', 3, 0, '#505050'), ('2', 3, 1, '#505050'), ('3', 3, 2, '#505050'), ('-', 3, 3, '#FF9500'),
    ('0', 4, 0, '#505050'), ('.', 4, 1, '#505050'), ('+', 4, 2, '#FF9500'), ('=', 4, 3, '#FF9500'),
]

for (text, row, col, color) in buttons:
    canvas = tk.Canvas(root, width=100, height=100, bg="black", highlightthickness=0)
    create_round_button(canvas, text, row, col, lambda t=text: button_click(t) if t != '=' else calculate, color, "white")

canvas = tk.Canvas(root, width=100, height=100, bg="black", highlightthickness=0)
create_round_button(canvas, 'C', 0, 3, clear_display, '#FF9500', "white")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
