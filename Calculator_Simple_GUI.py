#Calculator program with GUI

import tkinter as tk
import math as mt

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create entry widet to display input/output
        self.display = tk.Entry(master, width=18, justify='right', font=('Console', 22))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

        # Create buttons
        button_list = [
            'C', 'sqrt', 'expn', '%',
            '7', '8', '9', '+', 
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            '0', '.', '=', '/'
            ]
        
        r = 1
        c = 0
        for b in button_list:
            # Define button properties
            cmd = lambda x=b: self.click(x)
            tk.Button(master, text=b, width=7, height=2, font=('Console', 12), command=cmd)\
              .grid(row=r, column=c, padx=1, pady=1)
            c += 1
            r += 0
            if c > 3:
                c = 0
                r += 1

        # Bind keyboard input
        master.bind('<Key>', self.key_input)

    def click(self, key):
        if key == '=':
            # Calculate result
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            
        elif key == 'C':
            # Clear display
            self.display.delete(0, tk.END)

        elif key == 'sqrt':
            # Calculate result
            value = float(self.display.get())
            result = mt.sqrt(value)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))

        elif key == 'expn':
            # Handle exponentiation
            self.display.insert(tk.END, '**')

        elif key == '%':
            # Calculate percentage
            expression = self.display.get()
            if '+' in expression:
                parts = expression.split('+')
                value = float(parts[0])
                percent = float(parts[1])
                result = value * (1 + percent/100)
            elif '-' in expression:
                parts = expression.split('-')
                value = float(parts[0])
                percent = float(parts[1])
                result = value * (1 - percent/100)
            elif '*' in expression:
                parts = expression.split('*')
                value = float(parts[0])
                percent = float(parts[1])
                result = value * percent/100
            elif '/' in expression:
                parts = expression.split('/')
                value = float(parts[0])
                percent = float(parts[1])
                result = value / percent*100
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))

        else:
            # Add key to display
            self.display.insert(tk.END, key)

    def key_input(self, event):
        # Convert key press to string
        key = str(event.char)

        # Handle numeric input
        if key.isdigit() or key == ".":
            self.click(key)
        
        # Handle operator input
        elif key in ['+', '-', '*', '/', '%']:
            self.click(key)

        # Handle equals key
        elif key == '\r':
            self.click('=')

        # Handle clear key ("u00.." for unicode, "x.." for Python. '\x08' - backspace, '\x1b' - escape)
        elif key in ['\u0008', '\u001b', 'c']:
            self.click('C')

        # Handle exponentiation key
        elif key == "e":
            self.click('**')

        # Handle sqrt key
        elif key == "s":
            self.click('sqrt')

# Create main window
root = tk.Tk()

# Create calculator instance
calc = Calculator(root)

# Run the program
root.mainloop()
