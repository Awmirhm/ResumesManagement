from tkinter import Frame, Button, Label, LabelFrame, Canvas
from tkinter.font import Font
from PIL import Image, ImageTk
from BusinessLogicLayer.admin_business import AdminBusiness


class HomeFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.view = view

        self.current_user = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.font = Font(family="Comic Sans MS", size=20, weight="bold")

        self.font_label = Font(family="Serif", size=14, weight="bold")

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
        self.header.grid_columnconfigure(0, weight=1)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), ipadx=500, ipady=250)

        # Resumes Button
        self.image_resumes_button_tk = ImageTk.PhotoImage(
            Image.open("Images/personal-data_8346012.png").resize(size=(100, 100)))

        self.resumes_button = Button(self.header, image=str(self.image_resumes_button_tk), text="Resumes",
                                     compound="top", borderwidth=0, activebackground="#191919", background="#191919",
                                     font=self.font_label, pady=10, foreground="#FFD369", activeforeground="#C84B31"
                                     , command=self.resumes_button_clicked)
        self.resumes_button.grid(row=0, column=0, padx=(10, 10), pady=(30, 10), sticky="ew")

        # Admin Profile Button
        self.image_profile_button_tk = ImageTk.PhotoImage(
            Image.open("Images/user_5037329.png").resize(
                size=(100, 100)
            ))

        self.admin_profile_button = Button(self.header, image=str(self.image_profile_button_tk),
                                           borderwidth=0, background="#191919", activebackground="#191919",
                                           pady=10, font=self.font_label, text="Profile", compound="top",
                                           foreground="#FFD369", activeforeground="#C84B31",
                                           command=self.admin_profile_button_clicked)
        self.admin_profile_button.grid(row=1, column=0, padx=(10, 10), pady=(30, 10), sticky="ew")

        # Back
        self.image_back_button_tk = ImageTk.PhotoImage(
            Image.open("Images/back_14018855.png").resize(size=(100, 100)))

        self.back = Button(self.header, text="Back", command=self.back_button_clicked, borderwidth=0,
                           image=str(self.image_back_button_tk), background="#191919",
                           activebackground="#191919")
        self.back.grid(row=2, column=0, padx=(10, 10), pady=(10, 10), sticky="ew")

    def size(self, event):
        self.image = Image.open("Images/black-abstract-dark-3840x2160-9729.jpg")
        self.image_resize = self.image.resize(size=(event.width, event.height))
        self.image_tk = ImageTk.PhotoImage(self.image_resize)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor="nw")

    def set_current_user(self, user):
        self.current_user = user
        self.header.config(text=f"Wellcome, {self.current_user.firstname} {self.current_user.lastname}")

    def resumes_button_clicked(self):
        self.view.switch("show_resumes")

    def admin_profile_button_clicked(self):
        profile_frame = self.view.switch("profile")
        profile_frame.set_current_user_for_profile(self.current_user)

    def back_button_clicked(self):
        self.view.switch("login")
