import tkinter as tk
from app_window import AppWindow

class InteractionApp(AppWindow):

    def on_button_click(self):
        self.label.config(text=self.entry.get())
        self.entry.delete(0, tk.END)

    def init_widgets(self):
        self.entry = tk.Entry(self.root, bg='white')
        self.entry.pack()
        self.entry.focus()
        self.button = tk.Button(self.root, text="Klick mich!", command=self.on_button_click)
        self.button.pack()
        self.label = tk.Label(self.root, text="")
        self.label.pack()


if __name__ == "__main__":
    app = InteractionApp(200, 100, "Interaktion")
    app.run()
