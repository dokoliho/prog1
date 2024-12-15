import tkinter as tk
from app_window import AppWindow


POSSIBLE_SIDES = [tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT]
POSSIBLE_COLORS = ["red", "green", "blue", "orange"]

class PackApp(AppWindow):
    def init_widgets(self):
        for i in range(20):
            current_side =  POSSIBLE_SIDES[i % 4]
            label = tk.Label(self.root, text=f"{i}", bg=POSSIBLE_COLORS[i % 4])
            label.pack(side=current_side, fill=tk.BOTH)

if __name__ == "__main__":
    app = PackApp(300, 300, "Pack")
    app.run()
