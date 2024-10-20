import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
from PIL import Image, ImageTk

window = tk.Tk()
window.title('muhammad rafliansyah')

background_image = Image.open("C:\\Users\\ACER\\Downloads\\vvfvsjhfas.jpg")
background_image = background_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()), Image.Resampling.LANCZOS)
bg_image = ImageTk.PhotoImage(background_image)

canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

window.attributes('-fullscreen', True)

frame = tk.Frame(master=window, bg="grey", padx=10)
frame.place(relx=0.5, rely=0.5, anchor='center')

entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=20, width=30)
entry.grid(row=0, column=0, columnspan=5, ipady=2, pady=2, sticky="nsew")

def myclick(number):
    entry.insert(tk.END, number)

def equal():
    try:
        y = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0, tk.END)

def percent():
    try:
        current_value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(current_value / 100))
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def delete():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])  # Remove last character

def add_decimal():
    if '.' not in entry.get():
        entry.insert(tk.END, '.')

def toggle_sign():
    current_text = entry.get()
    if current_text:
        try:
            if current_text[0] == '-':
                entry.delete(0)
                entry.insert(0, current_text[1:])  # Remove the minus sign
            else:
                entry.delete(0)
                entry.insert(0, '-' + current_text)  # Add the minus sign
        except ValueError:
            tkinter.messagebox.showinfo("Error", "Invalid Input")

button_1 = tk.Button(master=frame, text='1', padx=15, pady=5, borderwidth=12, font=(50), command=lambda: myclick(1))
button_1.grid(row=4, column=0, pady=2, sticky="nsew")
button_2 = tk.Button(master=frame, text='2', padx=15, pady=5, borderwidth=12, font=(50), command=lambda: myclick(2))
button_2.grid(row=4, column=1, pady=2, sticky="nsew")
button_3 = tk.Button(master=frame, text='3', padx=15, pady=5, borderwidth=12, font=(50), command=lambda: myclick(3))
button_3.grid(row=4, column=2, pady=2, sticky="nsew")
button_4 = tk.Button(master=frame, text='4', padx=15, pady=5, borderwidth=12, font=(50), command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=2, sticky="nsew")
button_5 = tk.Button(master=frame, text='5', padx=15, pady=5, borderwidth=12, font=(50), command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=2, sticky="nsew")
button_6 = tk.Button(master=frame, text='6', padx=15, pady=5, borderwidth=12, font=(50), command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=2, sticky="nsew")
button_7 = tk.Button(master=frame, text='7', padx=15, pady=5, borderwidth=12, font=(50), command=lambda: myclick(7))
button_7.grid(row=3, column=0, pady=2, sticky="nsew")
button_8 = tk.Button(master=frame, text='8', padx=15, pady=5, borderwidth=12, font=(50), command=lambda: myclick(8))
button_8.grid(row=3, column=1, pady=2, sticky="nsew")
button_9 = tk.Button(master=frame, text='9', padx=15, pady=5, borderwidth=12, font=(50), command=lambda: myclick(9))
button_9.grid(row=3, column=2, pady=2, sticky="nsew")
button_0 = tk.Button(master=frame, text='0', padx=15, pady=5, borderwidth=12, font=(50), command=lambda: myclick(0))
button_0.grid(row=5, column=1, columnspan=2, pady=2, sticky="nsew")

button_add = tk.Button(master=frame, text="+", padx=15, pady=5, bg="orange", borderwidth=12, font=(50), command=lambda: myclick('+'))
button_add.grid(row=2, column=3, pady=2, sticky="nsew")
button_subtract = tk.Button(master=frame, text="-", padx=15, pady=5, bg="orange", borderwidth=12, font=(50), command=lambda: myclick('-'))
button_subtract.grid(row=3, column=3, pady=2, sticky="nsew")
button_multiply = tk.Button(master=frame, text="*", padx=15, pady=5, bg="orange", borderwidth=12, font=(50), command=lambda: myclick('*'))
button_multiply.grid(row=1, column=3, pady=2, sticky="nsew")
button_div = tk.Button(master=frame, text="/", padx=15, pady=5, bg="orange", borderwidth=12, font=(50), command=lambda: myclick('/'))
button_div.grid(row=1, column=2, pady=2, sticky="nsew")
button_clear = tk.Button(master=frame, text="C", padx=15, pady=5, bg="orange", borderwidth=12, command=clear)
button_clear.grid(row=1, column=0, columnspan=1, pady=2, sticky="nsew")
button_delete = tk.Button(master=frame, text="⌫", padx=15, pady=5, bg="orange", borderwidth=12, command=delete)
button_delete.grid(row=1, column=2, pady=2, sticky="nsew")
button_decimal = tk.Button(master=frame, text=",", padx=15, pady=5, bg="orange", borderwidth=12, command=add_decimal)
button_decimal.grid(row=4, column=3, pady=2, sticky="nsew")
button_sign = tk.Button(master=frame, text="±", padx=15, pady=5, bg="orange", borderwidth=12, command=toggle_sign)
button_sign.grid(row=5, column=0, pady=2, sticky="nsew")

button_equal = tk.Button(master=frame, text="=", padx=15, pady=5, bg="orange", borderwidth=12, command=equal)
button_equal.grid(row=5, column=3, columnspan=3, pady=2, sticky="nsew")
button_percent = tk.Button(master=frame, text="%", padx=15, pady=5, bg="orange", borderwidth=12, command=percent)
button_percent.grid(row=1, column=1, pady=2, sticky="nsew")

for i in range(8):
    frame.grid_rowconfigure(i, weight=1)
for j in range(4):
    frame.grid_columnconfigure(j, weight=1)

def toggle_fullscreen(event=None):
    is_fullscreen = window.attributes('-fullscreen')
    window.attributes('-fullscreen', not is_fullscreen)

def end_fullscreen(event=None):
    window.attributes('-fullscreen', False)

window.bind('<F11>', toggle_fullscreen)
window.bind('<Escape>', end_fullscreen)

window.mainloop()
