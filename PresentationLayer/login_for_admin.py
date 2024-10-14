from tkinter import Frame, LabelFrame, Label, Entry, Button, messagebox, END, Canvas
from tkinter.font import Font
from PIL import Image, ImageTk
from BusinessLogicLayer.admin_business import AdminBusiness


class LoginAdmin(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.admin_business = AdminBusiness()

        self.view = view

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
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), ipadx=500, ipady=250)

        # Username
        self.username_label = Label(self.header, text="Username :", background="#191919", foreground="white",
                                    font=self.font_label)
        self.username_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.username_entry = Entry(self.header, borderwidth=2, font=self.font_entry)
        self.username_entry.focus()
        self.username_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Password
        self.password_label = Label(self.header, text="Password :", background="#191919", foreground="white",
                                    font=self.font_label)
        self.password_label.grid(row=1, column=0, padx=(10, 10), pady=(10, 0), sticky="w")

        self.password_entry = Entry(self.header, borderwidth=2, show="*", font=self.font_entry)
        self.password_entry.grid(row=1, column=1, padx=(0, 10), pady=(10, 0), sticky="ew")

        # Login Button
        self.image_save_button_tk = ImageTk.PhotoImage(
            Image.open("Images/login_14018816.png").resize(size=(100, 100)))

        self.login_button = Button(self.header, image=str(self.image_save_button_tk), borderwidth=0,
                                   background="#191919", activebackground="#191919", command=self.login_button_clicked)
        self.login_button.grid(row=2, column=1, padx=(0, 10), pady=(0, 0), sticky="w")

        # Back
        self.image_back_button_tk = ImageTk.PhotoImage(
            Image.open("Images/back_14018855.png").resize(size=(100, 100)))

        self.back = Button(self.header, text="Back", command=self.back_button_clicked, borderwidth=0,
                           image=str(self.image_back_button_tk), background="#191919",
                           activebackground="#191919")
        self.back.grid(row=3, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

    def size(self, event):
        self.image = Image.open("Images/black-abstract-dark-3840x2160-9729.jpg")
        self.image_resize = self.image.resize(size=(event.width, event.height))
        self.image_tk = ImageTk.PhotoImage(self.image_resize)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor="nw")

    def login_button_clicked(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        result = self.admin_business.login(username, password)
        user = result[0]
        error_message = result[1]

        if error_message:
            messagebox.showerror(title="Error", message=error_message)
        else:
            home_frame = self.view.switch("home")
            home_frame.set_current_user(user)
            self.username_entry.delete(0, END)
            self.password_entry.delete(0, END)
            self.username_entry.focus()

    def back_button_clicked(self):
        self.view.switch("main_page")
