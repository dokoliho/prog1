import tkinter as tk
from app_window import AppWindow


POSSIBLE_SIDES = [tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT]


class LayoutApp(AppWindow):
    def init_widgets(self):
        button1 = tk.Button(self.root, text="Oben")
        button1.pack(side=tk.TOP, pady=10)

        button2 = tk.Button(self.root, text="Unten")
        button2.pack(side=tk.BOTTOM, pady=10)

if __name__ == "__main__":
    app = LayoutApp(300, 150, "Layout")
    app.run()
