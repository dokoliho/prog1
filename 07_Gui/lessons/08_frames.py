import tkinter as tk
from app_window import AppWindow


POSSIBLE_SIDES = [tk.TOP, tk.BOTTOM, tk.LEFT, tk.RIGHT]


class FrameApp(AppWindow):
    def init_widgets(self):
        frame1 = tk.Frame(self.root, width=250, height=70, borderwidth = 1, relief="sunken")
        frame1.pack(pady=10, padx=10, fill=tk.X, expand=True)
        frame2 = tk.Frame(self.root,  width=250, height=70, borderwidth = 1, relief="sunken")
        frame2.pack(pady=10, padx=10, fill=tk.X, expand=True)
        frame3 = tk.Frame(self.root,  width=250, height=70, borderwidth = 1, relief="sunken")
        frame3.pack(pady=10, padx=10, fill= tk.X, expand=True)

        label11 = tk.Label(frame1, text="A", bg="lightblue")
        label11.pack(side=tk.LEFT, padx=20, pady=20)
        label12 = tk.Label(frame1, text="B", bg="lightblue")
        label12.pack(side=tk.LEFT, padx=20, pady=20)

        label21 = tk.Label(frame2, text="A", bg="lightgreen")
        label21.pack(side=tk.LEFT, padx=20, pady=20)
        label22 = tk.Label(frame2, text="B", bg="lightgreen")
        label22.pack(side=tk.RIGHT, padx=20, pady=20)

        label31 = tk.Label(frame3, text="A", bg="lightcoral")
        label31.pack(side=tk.RIGHT, padx=20, pady=20)
        label32 = tk.Label(frame3, text="B", bg="lightcoral")
        label32.pack(side=tk.RIGHT, padx=20, pady=20)


if __name__ == "__main__":
    app = FrameApp(300, 300, "Frames")
    app.run()
