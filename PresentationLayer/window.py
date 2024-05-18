from tkinter import Tk, Canvas
from PIL import Image, ImageTk


class Window(Tk):
    def __init__(self, weight=1200, height=800):
        super().__init__()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title("Resumes Management")
        icon_image = Image.open("C:/Users/Maxsys/Pictures/pngtree-vector-resume-icon-png-image_953181.jpg").resize(
            size=(500, 500))
        icon_image_tk = ImageTk.PhotoImage(icon_image)
        self.wm_iconphoto(False, str(icon_image_tk))

        self.geometry(f"{weight}x{height}")

        self.canvas = Canvas(self, highlightthickness=0, bd=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.image = None
        self.image_resize = None
        self.image_tk = None

        self.canvas.bind("<Configure>", self.size)

    def show(self):
        self.mainloop()

    def size(self, event):
        self.image = Image.open("C:/Users/Maxsys/Pictures/flat-lay-desk-concept-with-copy-space_23-2148459512.jpg")
        self.image_resize = self.image.resize(size=(event.width, event.height))
        self.image_tk = ImageTk.PhotoImage(self.image_resize)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor="nw")
