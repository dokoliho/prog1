import tkinter as tk
from app_window import AppWindow


POSSIBLE_SIDES = [tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT]


class GridApp(AppWindow):
    def init_widgets(self):
        for row in range(3):
            for col in range(3):
                label = tk.Label(self.root, text=f"{row}-{col}")
                label.grid(row=row, column=col)

if __name__ == "__main__":
    app = GridApp(300, 300, "Grid")
    app.run()
