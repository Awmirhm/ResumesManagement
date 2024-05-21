from tkinter import Frame, Canvas, LabelFrame, Label, Entry, END, Button, messagebox
from tkinter.font import Font
from PIL import Image, ImageTk


class ProfileFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.current_user = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.font = Font(family="Comic Sans MS", size=20, weight="bold")

        self.font_label = Font(family="Serif", size=14, weight="bold")

        self.font_entry = Font(family="Serif", size=12, weight="bold")

        self.canvas = Canvas(self, highlightthickness=0, bd=0)
        self.canvas.grid_columnconfigure(0, weight=1)
        self.canvas.grid_rowconfigure(0, weight=1)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.image = None
        self.image_resize = None
        self.image_tk = None

        self.canvas.bind("<Configure>", self.size)

        self.header = LabelFrame(self.canvas, text="Login", labelanchor="n", borderwidth=0, font=self.font,
                                 background="#191919", foreground="white")
        self.header.grid_columnconfigure(1, weight=1)
        self.header.grid_columnconfigure(3, weight=1)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), ipadx=500, ipady=250)

        # First Name
        self.firstname_label = Label(self.header, text="First Name :", background="#191919", foreground="white",
                                     font=self.font_label)
        self.firstname_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.firstname_entry = Entry(self.header, font=self.font_entry)
        self.firstname_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Last Name
        self.lastname_label = Label(self.header, text="Last Name :", background="#191919", foreground="white",
                                    font=self.font_label)
        self.lastname_label.grid(row=0, column=2, padx=(10, 10), pady=(10, 10), sticky="w")

        self.lastname_entry = Entry(self.header, font=self.font_entry)
        self.lastname_entry.grid(row=0, column=3, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Username
        self.username_label = Label(self.header, text="Username :", background="#191919", foreground="white",
                                    font=self.font_label)
        self.username_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 10))

        self.username_entry = Entry(self.header, font=self.font_entry)
        self.username_entry.grid(row=1, column=1, columnspan=3, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Back To Home Button
        self.image_home_button_tk = ImageTk.PhotoImage(Image.open("C:/Users/Maxsys/Pictures/home_14018833.png").resize(
            size=(100, 100)
        ))

        self.back_to_home_page_button = Button(self.header, image=str(self.image_home_button_tk), borderwidth=0,
                                               background="#191919", activebackground="#191919",
                                               command=self.back_to_home_page_button_clicked)
        self.back_to_home_page_button.grid(row=2, column=1, columnspan=3, padx=(0, 10), pady=(10, 10), sticky="ew")

    def size(self, event):
        self.image = Image.open("C:/Users/Maxsys/Pictures/black-abstract-dark-3840x2160-9729.jpg")
        self.image_resize = self.image.resize(size=(event.width, event.height))
        self.image_tk = ImageTk.PhotoImage(self.image_resize)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor="nw")

    def set_current_user_for_profile(self, user):
        self.current_user = user

        self.firstname_entry.insert(0, str(self.current_user.firstname))
        self.lastname_entry.insert(0, str(self.current_user.lastname))
        self.username_entry.insert(0, str(self.current_user.username))

    def back_to_home_page_button_clicked(self):
        self.view.switch("home")
