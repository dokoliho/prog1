import tkinter as tk
from app_window import AppWindow

class ListboxApp(AppWindow):

    def on_button_click(self):
        self.listbox.insert(tk.END, self.entry.get())
        print(self.listbox.get(0, tk.END))
        self.entry.delete(0, tk.END)

    def init_widgets(self):
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack()
        self.entry = tk.Entry(self.root, bg='white')
        self.entry.pack()
        self.entry.focus()
        self.button = tk.Button(self.root, text="Hinzufügen", command=self.on_button_click)
        self.button.pack()


if __name__ == "__main__":
    app = ListboxApp(200, 240, "Listbox")
    app.run()
