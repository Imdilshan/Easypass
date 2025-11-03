from tkinter import *
from tkinter import ttk # Step 1: Import ttk
from random import choice
from tkinter import messagebox

BG_COLOR = "#202124"
SURFACE_COLOR = "#303134"
TEXT_COLOR = "#E8EAED"
ACCENT_COLOR = "#8AB4F8"
BUTTON_TEXT_COLOR = "#202124"

root = Tk()
root.title('Strong Password Generator')
root.geometry("550x450")
root.configure(bg=BG_COLOR)

style = ttk.Style(root)
style.theme_use('clam') 

style.configure('Accent.TButton', 
    background=ACCENT_COLOR, 
    foreground=BUTTON_TEXT_COLOR,
    font=('Roboto', 11, 'bold'),
    borderwidth=0,
    relief='flat'
)
style.map('Accent.TButton', 
    background=[('active', '#A4C2F4')] 
)

style.configure('Secondary.TButton', 
    background=BG_COLOR, 
    foreground=ACCENT_COLOR,
    font=('Roboto', 11, 'bold'),
    borderwidth=0,
    relief='flat'
)
style.map('Secondary.TButton', 
    background=[('active', SURFACE_COLOR)],
    foreground=[('active', ACCENT_COLOR)]
)

def new_rand():
    pw_entry.config(state='normal')
    pw_entry.delete(0, END)
    try:
        pw_length = int(length_entry.get())
        if pw_length <= 0: raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid password length.")
        return
    char_pool = ""
    if var_lower.get(): char_pool += "abcdefghijklmnopqrstuvwxyz"
    if var_upper.get(): char_pool += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if var_numbers.get(): char_pool += "0123456789"
    if var_special.get(): char_pool += "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    if not char_pool:
        messagebox.showerror("No Characters Selected", "Please select at least one character type.")
        return
    password = ''.join(choice(char_pool) for _ in range(pw_length))
    pw_entry.insert(0, password)
    pw_entry.config(state='readonly')

def clipper():
    password = pw_entry.get()
    if not password:
        messagebox.showwarning("Empty Password", "There is no password to copy.")
        return
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied!", "Password copied to clipboard!")

length_frame = LabelFrame(root, text="Password Length", bg=BG_COLOR, fg=TEXT_COLOR, font=("Roboto", 11), bd=0)
length_frame.pack(pady=20)
length_entry = Entry(length_frame, font=("Roboto", 20), width=5, justify='center', bg=SURFACE_COLOR, fg=TEXT_COLOR, insertbackground=ACCENT_COLOR, bd=0, highlightthickness=1, highlightbackground=SURFACE_COLOR, highlightcolor=ACCENT_COLOR)
length_entry.pack(pady=10, padx=20)
length_entry.insert(0, "15")

options_frame = LabelFrame(root, text="Include Characters", bg=BG_COLOR, fg=TEXT_COLOR, font=("Roboto", 11), bd=0)
options_frame.pack(pady=10)

var_lower, var_upper = BooleanVar(value=True), BooleanVar(value=True)
var_numbers, var_special = BooleanVar(value=True), BooleanVar(value=True)

check_style = {"bg": BG_COLOR, "fg": TEXT_COLOR, "selectcolor": SURFACE_COLOR, "activebackground": BG_COLOR, "activeforeground": TEXT_COLOR, "font": ("Roboto", 10)}
Checkbutton(options_frame, text="Lowercase", variable=var_lower, **check_style).grid(row=0, column=0, padx=10, pady=5, sticky='w')
Checkbutton(options_frame, text="Uppercase", variable=var_upper, **check_style).grid(row=0, column=1, padx=10, pady=5, sticky='w')
Checkbutton(options_frame, text="Numbers", variable=var_numbers, **check_style).grid(row=1, column=0, padx=10, pady=5, sticky='w')
Checkbutton(options_frame, text="Special", variable=var_special, **check_style).grid(row=1, column=1, padx=10, pady=5, sticky='w')

pw_entry = Entry(root, font=("Roboto", 24), bd=0, bg=SURFACE_COLOR, fg=TEXT_COLOR, justify='center', state='readonly', readonlybackground=SURFACE_COLOR)
pw_entry.pack(pady=20, padx=20, fill='x', ipady=5)

button_frame = Frame(root, bg=BG_COLOR)
button_frame.pack(pady=10)

generate_button = ttk.Button(button_frame, text="Generate Password", command=new_rand, style='Accent.TButton', takefocus=False)
generate_button.grid(row=0, column=0, padx=10, ipady=4)

copy_button = ttk.Button(button_frame, text="Copy Password", command=clipper, style='Secondary.TButton', takefocus=False)
copy_button.grid(row=0, column=1, padx=10, ipady=4)

root.mainloop()
