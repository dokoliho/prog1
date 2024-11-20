import tkinter as tk
from app_window import AppWindow

class LabelApp(AppWindow):
    def init_widgets(self):
        label = tk.Label(self.root, text="Textlabel")
        label.pack()

if __name__ == "__main__":
    app = LabelApp(200, 100, "Label")
    app.run()
