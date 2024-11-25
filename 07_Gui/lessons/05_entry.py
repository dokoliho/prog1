import tkinter as tk
from app_window import AppWindow

class EntryApp(AppWindow):
    def init_widgets(self):
        entry = tk.Entry(self.root, bg='white')
        entry.pack()
        entry.focus()

if __name__ == "__main__":
    app = EntryApp(200, 100, "Entry")
    app.run()
