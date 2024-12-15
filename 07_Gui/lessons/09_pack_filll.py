import tkinter as tk
from app_window import AppWindow

class LabelApp(AppWindow):
    def init_widgets(self):
        label1 = tk.Label(self.root, text="Oben", bg="lightblue")
        label1.pack(side=tk.TOP, fill=tk.NONE)

        #label2 = tk.Label(self.root, text="Mitte", bg="lightgreen")
        #label2.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        #label3 = tk.Label(self.root, text="Unten", bg="lightcoral")
        #label3.pack(side=tk.TOP, fill=tk.X)

if __name__ == "__main__":
    app = LabelApp(200, 100, "Label")
    app.run()
