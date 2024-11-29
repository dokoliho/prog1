import tkinter as tk
from app_window import AppWindow

class ShoppingList(AppWindow):
    def init_widgets(self):
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=5)
        self.add_button = tk.Button(self.root, text="Hinzufügen", command=self.add_item)
        self.add_button.pack(padx=5)
        self.listbox = tk.Listbox(self.root, height=10, width=40)
        self.listbox.pack(pady=10)
        self.remove_button = tk.Button(self.root, text="Entfernen", command=self.remove_item)
        self.remove_button.pack(pady=10)

    def add_item(self):
        item = self.entry.get()
        if item.strip():  # Leere Eingaben ignorieren
            self.listbox.insert(tk.END, item)
            self.entry.delete(0, tk.END)

    def remove_item(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)

if __name__ == "__main__":
    app = ShoppingList(400, 300, "Einkaufsliste")
    app.run()