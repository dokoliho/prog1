import tkinter as tk
from app_window import AppWindow


class GridApp(AppWindow):

    def init_widgets(self, width, height, title):
        super().__init__(width, height, title)
        self.entry_name = None
        self.entry_email = None
        self.entry_phone = None

    def save_data(self):
        with open("data.txt", "a") as file:
            file.write(f"{self.entry_name.get()}, {self.entry_email.get()}, {self.entry_phone.get()}\n")
        self.root.destroy()

    def init_widgets(self):
        label_name = tk.Label(self.root, text="Name:")
        label_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        label_email = tk.Label(self.root, text="E-Mail:")
        label_email.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        label_phone = tk.Label(self.root, text="Telefon:")
        label_phone.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        # Eingabefelder
        self.entry_name = tk.Entry(self.root, width=30)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)
        self.entry_email = tk.Entry(self.root, width=30)
        self.entry_email.grid(row=1, column=1, padx=10, pady=5)
        self.entry_phone = tk.Entry(self.root, width=30)
        self.entry_phone.grid(row=2, column=1, padx=10, pady=5)
        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.grid(row=3, column=1, sticky="e", pady=10)
        button_save = tk.Button(button_frame, text="Speichern", command=self.save_data)
        button_save.pack(side=tk.RIGHT)
        button_abbruch = tk.Button(button_frame, text="Abbrechen", command=self.root.destroy)
        button_abbruch.pack(side=tk.RIGHT)



if __name__ == "__main__":
    app = GridApp(400, 170, "Eingabemaske")
    app.run()
