import tkinter as tk
from app_window import AppWindow


class CloseApp(AppWindow):

    def __init__(self, width, height, title="AppWindow"):
        super().__init__(width, height, title)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")


    def on_button_click(self):
        self.root.destroy()

    def init_widgets(self):
        button = tk.Button(self.root, text="Ok", command=self.on_button_click)
        button.pack(pady=20)

if __name__ == "__main__":
    app = CloseApp(200, 100, "Close")
    app.run()

