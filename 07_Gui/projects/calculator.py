import tkinter as tk
from app_window import AppWindow

class CalculatorApp(AppWindow):
    def __init__(self, width, height, title="Calculator"):
        super().__init__(width, height, title)
        self.accumulator = 0  # Akkumulator für Berechnungen
        self.current_operator = None  # Speichert die aktuelle Operation
        self.new_input = True  # Gibt an, ob der Benutzer eine neue Zahl eingibt

    def init_widgets(self):
        self.display = tk.Entry(self.root, font=("Arial", 18), justify="right")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        self.create_buttons()
        for i in range(6):  # 5 Zeilen (0-5)
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):  # 4 Spalten (0-3)
            self.root.grid_columnconfigure(i, weight=1)

    def create_buttons(self):
        button_config = [
            ("7", self.button_7, 1, 0), ("8", self.button_8, 1, 1), ("9", self.button_9, 1, 2),
            ("/", self.button_divide, 1, 3),
            ("4", self.button_4, 2, 0), ("5", self.button_5, 2, 1), ("6", self.button_6, 2, 2),
            ("*", self.button_multiply, 2, 3),
            ("1", self.button_1, 3, 0), ("2", self.button_2, 3, 1), ("3", self.button_3, 3, 2),
            ("-", self.button_subtract, 3, 3),
            ("0", self.button_0, 4, 0), (".", self.button_dot, 4, 1), ("C", self.clear, 4, 2),
            ("+", self.button_add, 4, 3),
        ]
        for text, command, row, col in button_config:
            btn = tk.Button(self.root, text=text, font=("Arial", 14), command=command)
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        equal_btn = tk.Button(self.root, text="=", font=("Arial", 14), command=self.calculate)
        equal_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

    # Zahlen- und Punkt-Buttons
    def button_0(self): self.add_to_display("0")
    def button_1(self): self.add_to_display("1")
    def button_2(self): self.add_to_display("2")
    def button_3(self): self.add_to_display("3")
    def button_4(self): self.add_to_display("4")
    def button_5(self): self.add_to_display("5")
    def button_6(self): self.add_to_display("6")
    def button_7(self): self.add_to_display("7")
    def button_8(self): self.add_to_display("8")
    def button_9(self): self.add_to_display("9")
    def button_dot(self): self.add_to_display(".")

    # Operatoren-Buttons
    def button_add(self): self.set_operator("+")
    def button_subtract(self): self.set_operator("-")
    def button_multiply(self): self.set_operator("*")
    def button_divide(self): self.set_operator("/")

    def add_to_display(self, value):
        if self.new_input:
            self.display.delete(0, tk.END)
            self.new_input = False
        self.display.insert(tk.END, value)

    def set_operator(self, operator):
        self.current_operator = operator
        self.accumulator = float(self.display.get())
        self.new_input = True

    def clear(self):
        self.display.delete(0, tk.END)
        self.accumulator = 0
        self.current_operator = None
        self.new_input = True

    def calculate(self):
        if self.current_operator is not None:
            current_value = float(self.display.get())
            if self.current_operator == "+":
                self.accumulator += current_value
            elif self.current_operator == "-":
                self.accumulator -= current_value
            elif self.current_operator == "*":
                self.accumulator *= current_value
            elif self.current_operator == "/":
                if current_value != 0:
                    self.accumulator /= current_value
                else:
                    self.display.delete(0, tk.END)
                    self.display.insert(0, "Error")
                    return
            self.display.delete(0, tk.END)
            self.display.insert(0, str(self.accumulator))
            self.current_operator = None
            self.new_input = True


if __name__ == "__main__":
    app = CalculatorApp(300, 400, "Taschenrechner")
    app.run()
