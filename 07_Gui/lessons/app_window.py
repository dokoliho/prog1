import tkinter as tk

class AppWindow:
    def __init__(self, width, height, title="AppWindow"):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}")

    def run(self):
        self.init_widgets()
        self.root.mainloop()
        self.close()

    def init_widgets(self):
        pass

    def close(self):
        pass


if __name__ == "__main__":
    app = AppWindow(200, 100, "Hello World")
    app.run()