import tkinter as tk
from app_window import AppWindow


POSSIBLE_SIDES = [tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT]


class GridApp(AppWindow):

    def init_widgets(self):

        for i in range(3):
            self.root.grid_rowconfigure(i, weight=i)
            self.root.grid_columnconfigure(i, weight=1)

        for row in range(3):
            for col in range(3):
                px = 20 if row == col else 10
                py = 20 if row == col else 10
                st = None
                if row == 0 and col == 1: st = tk.N
                if row == 2 and col == 1: st = tk.S
                if row == 1 and col == 0: st = tk.W
                if row == 1 and col == 2: st = tk.E
                text = f"sticky={st}" if st else "Center"
                label = tk.Label(self.root, text=text, bg="lightblue")
                label.grid(row=row, column=col, pady=py, padx=px, sticky=st)


if __name__ == "__main__":
    app = GridApp(270, 200, "Grid")
    app.run()
