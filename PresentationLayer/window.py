from tkinter import Tk, Canvas, Button
from PIL import Image, ImageTk


class Window(Tk):
    def __init__(self, weight=1600, height=1200):
        super().__init__()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title("Resumes Management")
        icon_image = Image.open("Images/pngtree-vector-resume-icon-png-image_953181.jpg").resize(
            size=(500, 500))
        icon_image_tk = ImageTk.PhotoImage(icon_image)
        self.wm_iconphoto(False, str(icon_image_tk))

        self.geometry(f"{weight}x{height}")

    def show(self):
        self.mainloop()
