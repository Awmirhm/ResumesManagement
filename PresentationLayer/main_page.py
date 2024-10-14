from tkinter import Frame, Label, Button, Canvas
from tkinter.font import Font
from PIL import Image, ImageTk


class MainPage(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.window = window

        self.view = view

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.canvas = Canvas(self, highlightthickness=0, bd=0)
        self.canvas.grid(row=0, column=1, sticky="nsew")

        self.image = None
        self.image_resize = None
        self.image_tk = None

        self.canvas.bind("<Configure>", self.size)

        self.font = Font(family="Comic Sans MS", size=20, weight="bold")

        self.image_form_button_tk = ImageTk.PhotoImage(
            Image.open("Images/resume-icon-1586x2048-icyvzr1b.png").resize(size=(100, 100)))

        self.resumes_button = Button(self, text="Resumes", image=str(self.image_form_button_tk), borderwidth=0,
                                     compound="top", font=self.font, command=self.resumes_button_clicked)
        self.resumes_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nw")

        self.image_admin_button_tk = ImageTk.PhotoImage(
            Image.open(
                "Images/1707088.png").resize(
                size=(100, 100)))

        self.admin_button = Button(self, text="Admin", image=str(self.image_admin_button_tk), borderwidth=0,
                                   compound="top", font=self.font, command=self.admin_button_clicked)
        self.admin_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.image_exit_button_tk = ImageTk.PhotoImage(
            Image.open("Images/1824420.png").resize(size=(100, 100)))

        self.exit_button = Button(self, text="Exit", image=str(self.image_exit_button_tk), borderwidth=0,
                                  compound="top", font=self.font, command=self.exit_button_clicked)
        self.exit_button.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="sw")

    def size(self, event):
        self.image = Image.open("Images/black-abstract-dark-3840x2160-9729.jpg")
        self.image_resize = self.image.resize(size=(event.width, event.height))
        self.image_tk = ImageTk.PhotoImage(self.image_resize)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor="nw")

    def resumes_button_clicked(self):
        self.view.switch("resumes")

    def admin_button_clicked(self):
        self.view.switch("login")

    def exit_button_clicked(self):
        self.window.destroy()
