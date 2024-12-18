import tkinter as tk
from app_window import AppWindow

class GridApp(AppWindow):
    def init_widgets(self):
        for row in range(3):
            for col in range(3):
                label = tk.Label(self.root, text=f"Zeile {row}, Spalte {col}")
                label.grid(row=row, column=col, pady=10, padx=10)


if __name__ == "__main__":
    app = GridApp(400, 150, "Grid")
    app.run()
