import tkinter as tk
from tkinter import filedialog
from app_window import AppWindow

class Editor(AppWindow):
    def init_widgets(self):
        self.text_area = tk.Text(self.root, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        self.load_button = tk.Button(self.root, text="Laden", command=self.load_file)
        self.load_button.pack(pady=5)
        self.save_button = tk.Button(self.root, text="Speichern", command=self.save_file)
        self.save_button.pack(pady=5)

    def load_file(self):
        file_path = filedialog.askopenfilename()
        if file_path != None:  # Falls der Benutzer eine Datei ausgewählt hat
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
        )
        if file_path != None:  # Falls der Benutzer einen Speicherort gewählt hat
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)


if __name__ == "__main__":
    app = Editor(400, 450, "Editor")
    app.run()