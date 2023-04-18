#Calculator program with GUI

import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create entry widet to display input/output
        self.display = tk.Entry(master, width=20, justify='right', font=('Console', 12))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

        # Create buttons
        button_list = [
            '7', '8', '9', '+', 
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            '0', '.', '=', '/', 
            'C'
            ]
        
        r = 1
        c = 0
        for b in button_list:
            # Define button properties
            cmd = lambda x=b: self.click(x)
            tk.Button(master, text=b, width=4, height=1, font=('Console', 12), command=cmd)\
              .grid(row=r, column=c, padx=5, pady=5)
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

        # Handle clear key
        elif key == '\x08':
            self.click('C')

# Create main window
root = tk.Tk()

# Create calculator instance
calc = Calculator(root)

# Run the program
root.mainloop()
