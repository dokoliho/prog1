import tkinter as tk
from app_window import AppWindow


POSSIBLE_SIDES = [tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT]


class GridApp(AppWindow):
    def init_widgets(self):
        for row in range(3):
            for col in range(3):
                label = tk.Label(self.root, text=f"Zeile {row}, Spalte {col}")
                label.grid(row=row, column=col, pady=10, padx=10, sticky=tk.W)
 #       self.root.grid_rowconfigure(0, weight=1)  # Zeile 0 behält ihre Größe
 #       self.root.grid_rowconfigure(1, weight=1)  # Zeile 0 behält ihre Größe
 #       self.root.grid_rowconfigure(2, weight=1)  # Zeile 0 behält ihre Größe


if __name__ == "__main__":
    app = GridApp(300, 300, "Grid")
    app.run()
