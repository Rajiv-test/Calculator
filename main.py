from tkinter import *
from tkinter import ttk

def pressed(event=None):
    global first_number, operation  # Use global variables for state tracking
    
    key = event.char  # Get the pressed key (character)
    if key.isdigit():  # If the key is a digit, allow input
        entry.insert(END, key)
    elif key in ("+", "-", "*", "/"):  # If it's an operation
        label["text"]= " "+key+" "
        first_number = entry.get()  # Store the first number
        operation = key  # Store the selected operation
        entry.delete(0, END)  # Clear the entry widget for the second number
    elif key == "c":  # Clear for reset
        label["text"] = " C " 
        entry.delete(0, END)
        first_number = None
        operation = None
    return "break"

def equals(event=None):
    global first_number, operation  # Use global variables for state tracking
    
    try:
        
        second_number = entry.get()
        entry.delete(0,END)
        result = eval(first_number+operation+second_number)
        label["text"] = " = "
        entry.insert(END,str(result))
    except Exception as e:
        label["text"] = " X "
        entry.insert(END,f"Error")

root = Tk()
root.geometry("500x500")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=10)

input_box = ttk.Frame(root)
input_box.columnconfigure(0, weight=1)
input_box.rowconfigure(0, weight=1)
input_box.grid(row=0, column=0, sticky="NEWS", padx=5, pady=5)

entry = ttk.Entry(input_box,font=("Comic Sans",20))
entry.grid(row=0, column=0, sticky="NEWS",columnspan=1)
entry.bind("<Return>", equals)

label = ttk.Label(input_box,text=" Inp ",font=("Comic Sans MS", 18),relief="groove")
label.grid(row=0, column=1,sticky="NEWS", padx=5, pady=5,columnspan=1)
label.columnconfigure(1,weight=1)

buttons = ttk.Frame(root)
buttons.grid(row=1, column=0, sticky="NEWS", padx=2, pady=2)
for i in range(4):
    buttons.rowconfigure(i, weight=1)
    buttons.columnconfigure(i, weight=1)

button_texts = [
    "1", "2", "3", "c",
    "4", "5", "6", "+",
    "7", "8", "9", "-",
    "/", "*", "%", "="
]

row_num = 0
col_num = 0
style = ttk.Style()
style.configure("Special.TButton", font=("Comic Sans MS", 18)) 
for text in button_texts:
    
    button = ttk.Button(buttons, text=text,style="Special.TButton")
    button.grid(row=row_num, column=col_num, sticky="NEWS", padx=5, pady=5)
    
    # Bind "Return" to equals function
    if text == "=":
        root.bind("<Return>", equals)
    else:
        # Bind the button text to keypress on the root window
        root.bind(f"<Key-{text}>", pressed)
    
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1
root.bind("q", lambda event: root.destroy())
root.mainloop()