import tkinter as tk
from app_window import AppWindow


POSSIBLE_SIDES = [tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT]


class PackApp(AppWindow):
    def init_widgets(self):
        for i in range(20):
            current_side =  POSSIBLE_SIDES[i % 4]
            label = tk.Label(self.root, text=f"{i}")
            label.pack(side=current_side)

if __name__ == "__main__":
    app = PackApp(300, 300, "Pack")
    app.run()
