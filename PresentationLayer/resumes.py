from tkinter import Frame, LabelFrame, Label, Button, Entry, Canvas
from tkcalendar import DateEntry
from tkinter.font import Font
from datetime import date
from PIL import Image, ImageTk


class Resumes(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.canvas = Canvas(self, highlightthickness=0, bd=0)
        self.canvas.grid_columnconfigure(0, weight=1)
        self.canvas.grid_rowconfigure(0, weight=1)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.image = None
        self.image_resize = None
        self.image_tk = None

        self.canvas.bind("<Configure>", self.size)

        self.font = Font(family="Comic Sans MS", size=20, weight="bold")

        self.font_label = Font(family="Serif", size=14, weight="bold")

        self.header = LabelFrame(self.canvas, text="Form", borderwidth=0, background="#F39F5A", foreground="white",
                                 labelanchor="n", font=self.font)
        self.header.grid_columnconfigure(1, weight=1)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), ipadx=300, ipady=250)

        self.firstname_label = Label(self.header, text="First Name  :", background="#F39F5A", foreground="white",
                                     font=self.font_label)
        self.firstname_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.firstname_entry = Entry(self.header)
        self.firstname_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        self.lastname_label = Label(self.header, text="Last Name  :", background="#F39F5A", foreground="white",font=self.font_label)
        self.lastname_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.lastname_entry = Entry(self.header)
        self.lastname_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.birthday_label = Label(self.header, text="Birthday  :", background="#F39F5A", foreground="white",font=self.font_label)
        self.birthday_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.birthday_entry = DateEntry(self.header, date_pattern="yyyy-mm-dd")
        self.birthday_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.back = Button(self, text="Back", command=self.back_button, borderwidth=5)
        self.back.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="sew")

    def size(self, event):
        self.image = Image.open("C:/Users/Maxsys/Pictures/black-abstract-dark-3840x2160-9729.jpg")
        self.image_resize = self.image.resize(size=(event.width, event.height))
        self.image_tk = ImageTk.PhotoImage(self.image_resize)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor="nw")
        # self.canvas.create_window(0, 0, window=self.header, anchor="nw")

    def back_button(self):
        self.view.switch("main_page")
