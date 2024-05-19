from tkinter import Frame, LabelFrame, Label, Button, Entry, Canvas, Radiobutton, IntVar
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
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), ipadx=400, ipady=250)

        # First Name
        self.firstname_label = Label(self.header, text="First Name :", background="#F39F5A", foreground="white",
                                     font=self.font_label)
        self.firstname_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.firstname_entry = Entry(self.header, borderwidth=0)
        self.firstname_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Last Name
        self.lastname_label = Label(self.header, text="Last Name :", background="#F39F5A", foreground="white",
                                    font=self.font_label)
        self.lastname_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.lastname_entry = Entry(self.header, borderwidth=0)
        self.lastname_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Birthday
        self.birthday_label = Label(self.header, text="Birthday :", background="#F39F5A", foreground="white",
                                    font=self.font_label)
        self.birthday_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.birthday_entry = DateEntry(self.header, date_pattern="yyyy-mm-dd", borderwidth=0)
        self.birthday_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Gender
        self.gender_label = Label(self.header, text="Gender :", background="#F39F5A", foreground="white",
                                  font=self.font_label)
        self.gender_label.grid(row=3, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.gender_radio_button_var = IntVar(value=0)
        self.gender_radio_button_male = Radiobutton(self.header, text="Male", value=1,
                                                    variable=self.gender_radio_button_var, background="#F39F5A",
                                                    foreground="#31363F", borderwidth=0, font=self.font_label)
        self.gender_radio_button_male.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        self.gender_radio_button_female = Radiobutton(self.header, text="Female", value=2,
                                                      variable=self.gender_radio_button_var, background="#F39F5A",
                                                      foreground="#31363F", borderwidth=0, font=self.font_label)
        self.gender_radio_button_female.grid(row=3, column=1, padx=(100, 10), pady=(0, 10), sticky="w")

        # Skills
        self.skill_label = Label(self.header, text="Skills :", background="#F39F5A", foreground="white",
                                 font=self.font_label)
        self.skill_label.grid(row=4, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.skill_entry = Entry(self.header, borderwidth=0)
        self.skill_entry.grid(row=4, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Email
        self.email_label = Label(self.header, text="Email :", background="#F39F5A", foreground="white",
                                 font=self.font_label)
        self.email_label.grid(row=5, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.email_entry = Entry(self.header, borderwidth=0)
        self.email_entry.grid(row=5, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        self.back = Button(self, text="Back", command=self.back_button, borderwidth=5)
        self.back.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="sew")

    def size(self, event):
        self.image = Image.open("C:/Users/Maxsys/Pictures/black-abstract-dark-3840x2160-9729.jpg")
        self.image_resize = self.image.resize(size=(event.width, event.height))
        self.image_tk = ImageTk.PhotoImage(self.image_resize)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor="nw")

    def back_button(self):
        self.view.switch("main_page")