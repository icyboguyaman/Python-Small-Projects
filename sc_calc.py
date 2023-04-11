import tkinter as tk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Scientific Calculator")
        self.master.geometry("400x400")
        
        # Create the display widget
        self.display = tk.Entry(self.master, width=30, font=("Arial", 16), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Create the buttons
        buttons = [
            "sin", "cos", "tan", "log",
            "sqrt", "pi", "e", "x^2",
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            "(", ")", "=", "del",
        ]
        row = 1
        col = 0
        for button_text in buttons:
            if col == 4:
                row += 1
                col = 0
            button = tk.Button(self.master, text=button_text, width=5, height=2, font=("Arial", 12),
                               command=lambda button_text=button_text: self.handle_button_click(button_text))
            button.grid(row=row, column=col, padx=3, pady=3)
            col += 1

    def handle_button_click(self, button_text):
        if button_text == "C":
            self.display.delete(0, tk.END)
        elif button_text == "del":
            current_text = self.display.get()
            self.display.delete(len(current_text)-1, tk.END)
        elif button_text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif button_text == "sin":
            self.display.insert(tk.END, "math.sin(")
        elif button_text == "cos":
            self.display.insert(tk.END, "math.cos(")
        elif button_text == "tan":
            self.display.insert(tk.END, "math.tan(")
        elif button_text == "log":
            self.display.insert(tk.END, "math.log10(")
        elif button_text == "sqrt":
            self.display.insert(tk.END, "math.sqrt(")
        elif button_text == "pi":
            self.display.insert(tk.END, "math.pi")
        elif button_text == "e":
            self.display.insert(tk.END, "math.e")
        elif button_text == "x^2":
            self.display.insert(tk.END, "**2")
        else:
            self.display.insert(tk.END, button_text)

root = tk.Tk()
app = Calculator(root)
root.mainloop()
