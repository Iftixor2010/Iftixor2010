import tkinter as tk


root = tk.Tk()
root.title("Kalkulyator")
root.geometry("300x400")


entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(value))


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Xato")


def clear():
    entry.delete(0, tk.END)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, width=10, height=3, command=calculate)
    else:
        btn = tk.Button(root, text=button, width=10, height=3, command=lambda value=button: button_click(value))
    
    btn.grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


clear_button = tk.Button(root, text="C", width=10, height=3, command=clear)
clear_button.grid(row=row_val, column=0, columnspan=4)

root.mainloop()


