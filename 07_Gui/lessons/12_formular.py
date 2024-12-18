import tkinter as tk
from app_window import AppWindow


class GridApp(AppWindow):
    def init_widgets(self):
        label_name = tk.Label(self.root, text="Name:")
        label_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        label_email = tk.Label(self.root, text="E-Mail:")
        label_email.grid(row=1, column=0, sticky="w", padx=10, pady=5)
        label_phone = tk.Label(self.root, text="Telefon:")
        label_phone.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        # Eingabefelder
        entry_name = tk.Entry(self.root, width=30)
        entry_name.grid(row=0, column=1, padx=10, pady=5)
        entry_email = tk.Entry(self.root, width=30)
        entry_email.grid(row=1, column=1, padx=10, pady=5)
        entry_phone = tk.Entry(self.root, width=30)
        entry_phone.grid(row=2, column=1, padx=10, pady=5)


if __name__ == "__main__":
    app = GridApp(400, 150, "Eingabemaske")
    app.run()
