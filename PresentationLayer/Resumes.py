from tkinter import Frame, LabelFrame, Label, Button, Entry, Canvas
from tkcalendar import DateEntry
from datetime import date
from PIL import Image, ImageTk


class Resumes(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.canvas = Canvas(self, highlightthickness=0, bd=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.image = None
        self.image_resize = None
        self.image_tk = None

        self.canvas.bind("<Configure>", self.size)

        self.header = LabelFrame(self, text="Resumes", borderwidth=5)
        self.header.grid_columnconfigure(1, weight=1)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        self.firstname_label = Label(self.header, text="First Name  :")
        self.firstname_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.firstname_entry = Entry(self.header)
        self.firstname_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        self.lastname_label = Label(self.header, text="Last Name  :")
        self.lastname_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.lastname_entry = Entry(self.header)
        self.lastname_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.birthday_label = Label(self.header, text="Birthday  :")
        self.birthday_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.birthday_entry = DateEntry(self.header, date_pattern="yyyy-mm-dd")
        self.birthday_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.back = Button(self, text="Back", command=self.back_button, borderwidth=5)
        self.back.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="sew")

    def size(self, event):
        self.image = Image.open("C:/Users/Maxsys/Pictures/flat-lay-desk-concept-with-copy-space_23-2148459512.jpg")
        self.image_resize = self.image.resize(size=(event.width, event.height))
        self.image_tk = ImageTk.PhotoImage(self.image_resize)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor="nw")
        self.canvas.create_window(0, 0, window=self.header, anchor="nw")

    def back_button(self):
        self.view.switch("main_page")
