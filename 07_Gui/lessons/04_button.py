import tkinter as tk
from app_window import AppWindow

class ButtonApp(AppWindow):

    def on_button_click(self):
        print("Button clicked")

    def init_widgets(self):
        button = tk.Button(self.root, text="Klick mich!", command=self.on_button_click)
        button.pack()

if __name__ == "__main__":
    app = ButtonApp(200, 100, "Button")
    app.run()
