import tkinter as tk
from app_window import AppWindow


class CloseApp(AppWindow):

    def on_button_click(self):
        self.root.destroy()

    def init_widgets(self):
        button = tk.Button(self.root, text="Ok", command=self.on_button_click)
        button.pack(pady=20)

if __name__ == "__main__":
    app = CloseApp(200, 100, "Close")
    app.run()

