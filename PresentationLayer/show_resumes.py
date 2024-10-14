from tkinter import Frame, LabelFrame, Label, Entry, END, Canvas, Button, messagebox
from tkinter.font import Font
from io import BytesIO
from PIL import Image, ImageTk
from BusinessLogicLayer.form_business import FormIterator
from BusinessLogicLayer.form_business import FormBusiness
from CommonLayer.gender_data_type import Gender
from CommonLayer.status_data_type import Status


class ShowResumesFrame(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.form_business = FormBusiness()

        self.view = view

        self.window = window

        self.counter = 1

        self.firstname = None
        self.lastname = None
        self.birthday = None
        self.image_user = None
        self.image_user_tk = None
        self.gender = None
        self.skills = None
        self.email = None
        self.status = None

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

        self.header = LabelFrame(self.canvas, text="Resumes", labelanchor="n", borderwidth=0, font=self.font,
                                 background="#191919", foreground="white")
        self.header.grid_columnconfigure(1, weight=1)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), ipadx=500, ipady=250)

        # Firstname
        self.firstname_label = Label(self.header, text="First Name :", background="#191919", foreground="white",
                                     font=self.font_label)
        self.firstname_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.firstname_entry = Entry(self.header, borderwidth=2, background="#EAD7BB", font=self.font_entry)
        self.firstname_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Last Name
        self.lastname_label = Label(self.header, text="Last Name :", background="#191919", foreground="white",
                                    font=self.font_label)
        self.lastname_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.lastname_entry = Entry(self.header, borderwidth=2, background="#EAD7BB", font=self.font_entry)
        self.lastname_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Photo Label
        self.photo_label = Label(self.header, background="#191919")
        self.photo_label.grid(row=0, rowspan=3, column=2, columnspan=2, padx=(10, 10), pady=(0, 10))

        # Birthday
        self.birthday_label = Label(self.header, text="Birthday :", background="#191919", foreground="white",
                                    font=self.font_label)
        self.birthday_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.birthday_entry = Entry(self.header, font=self.font_entry, background="#EAD7BB", borderwidth=2)
        self.birthday_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Gender
        self.gender_label = Label(self.header, text="Gender :", background="#191919", foreground="white",
                                  font=self.font_label)
        self.gender_label.grid(row=3, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.gender_entry = Entry(self.header, borderwidth=2, background="#EAD7BB", font=self.font_entry)
        self.gender_entry.grid(row=3, column=1, columnspan=3, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Skills
        self.skill_label = Label(self.header, text="Skills :", background="#191919", foreground="white",
                                 font=self.font_label)
        self.skill_label.grid(row=4, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.skill_entry = Entry(self.header, borderwidth=2, background="#EAD7BB", font=self.font_entry)
        self.skill_entry.grid(row=4, column=1, columnspan=3, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Email
        self.email_label = Label(self.header, text="Email :", background="#191919", foreground="white",
                                 font=self.font_label)
        self.email_label.grid(row=5, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.email_entry = Entry(self.header, borderwidth=2, background="#EAD7BB", font=self.font_entry)
        self.email_entry.grid(row=5, column=1, columnspan=3, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Status
        self.status_label = Label(self.header, text="Status :", background="#191919", foreground="white",
                                  font=self.font_label)
        self.status_label.grid(row=6, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.status_entry = Entry(self.header, borderwidth=2, background="#EAD7BB", font=self.font_entry)
        self.status_entry.grid(row=6, column=1, columnspan=3, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Next Button
        self.image_next_button_tk = ImageTk.PhotoImage(
            Image.open("Images/next_14018853.png").resize(size=(100, 100)))
        self.next_button = Button(self.header, image=str(self.image_next_button_tk), background="#191919",
                                  activebackground="#191919", borderwidth=0, command=self.next_button_clicked)
        self.next_button.grid(row=7, column=3, padx=(0, 10), pady=(0, 10), sticky="ns")

        # Accept Button
        self.image_accept_button_tk = ImageTk.PhotoImage(
            Image.open("Images/like_6844679.png").resize(
                size=(100, 100)
            ))
        self.accept_button = Button(self.header, background="#191919", activebackground="#191919", borderwidth=0,
                                    image=str(self.image_accept_button_tk), text="Accept", compound="top",
                                    font=self.font_label, foreground="#1C82AD", activeforeground="#940B92"
                                    , command=self.accept_button_clicked)
        self.accept_button.grid(row=8, column=1, padx=(300, 0), pady=(0, 10), sticky="w")

        # Reject Button
        self.image_reject_button_tk = ImageTk.PhotoImage(
            Image.open("Images/dislike_6844686.png").resize(
                size=(100, 100)
            ))
        self.reject_button = Button(self.header, background="#191919", activebackground="#191919", borderwidth=0,
                                    image=str(self.image_reject_button_tk), text="Reject", compound="top",
                                    font=self.font_label, foreground="#1C82AD", activeforeground="#940B92",
                                    command=self.reject_button_clicked)
        self.reject_button.grid(row=8, column=1, padx=(0, 300), pady=(0, 10), sticky="e")

        # Back To Home Button
        self.image_home_button_tk = ImageTk.PhotoImage(Image.open("Images/home_14018833.png").resize(
            size=(100, 100)
        ))

        self.back_to_home_page_button = Button(self.header, image=str(self.image_home_button_tk), borderwidth=0,
                                               background="#191919", activebackground="#191919",
                                               command=self.back_to_home_page_button_clicked)
        self.back_to_home_page_button.grid(row=9, column=1, padx=(0, 0), pady=(50, 10), sticky="ew")

    def size(self, event):
        self.image = Image.open("Images/black-abstract-dark-3840x2160-9729.jpg")
        self.image_resize = self.image.resize(size=(event.width, event.height))
        self.image_tk = ImageTk.PhotoImage(self.image_resize)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor="nw")

    def next_button_clicked(self):
        self.firstname_entry.delete(0, END)
        self.lastname_entry.delete(0, END)
        self.birthday_entry.delete(0, END)
        self.photo_label.config(image="")
        self.gender_entry.delete(0, END)
        self.skill_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.status_entry.delete(0, END)
        try:
            while True:
                for item in FormIterator(self.counter):
                    self.firstname = item.firstname
                    self.lastname = item.lastname
                    self.birthday = item.birthday
                    self.image_user = item.image
                    data_gender = int(item.gender)
                    self.gender = Gender(data_gender)
                    self.skills = item.skills
                    self.email = item.email
                    data_status = int(item.status)
                    self.status = Status(data_status)

                    self.firstname_entry.insert(0, self.firstname)
                    self.lastname_entry.insert(0, self.lastname)
                    self.image_user_tk = ImageTk.PhotoImage(
                        Image.open(BytesIO(self.image_user)).resize(size=(200, 200)))
                    self.photo_label.config(image=str(self.image_user_tk))
                    self.birthday_entry.insert(0, item.birthday)
                    self.gender_entry.insert(0,
                                             f"{self.gender.name if self.gender == Gender.MALE else self.gender.name}")
                    self.skill_entry.insert(0, self.skills)
                    self.email_entry.insert(0, self.email)
                    self.status_entry.insert(0, f"{self.status.name if self.status == Status.NOT_CHECKED else
                    self.status.name if self.status == Status.ACCEPT else self.status.name}")
                    break
                self.counter += 1
                if self.firstname or self.lastname or self.image_user or self.gender or self.skills or self.email:
                    self.firstname = None
                    self.lastname = None
                    self.image_user = None
                    self.gender = None
                    self.skills = None
                    self.email = None
                    self.status = None
                    break
                else:
                    raise IndexError
        except IndexError:
            messagebox.showwarning(title="Warning",
                                   message=f"There is no resume to display!\nPlease return to the main page. ")

    def accept_button_clicked(self):
        self.status_entry.delete(0, END)
        self.form_business.update_status_to_accept(self.counter - 1)
        accept = Status.ACCEPT
        self.status_entry.insert(0, str(accept.name))

    def reject_button_clicked(self):
        self.status_entry.delete(0, END)
        self.form_business.update_status_to_reject(self.counter - 1)
        reject = Status.REJECT
        self.status_entry.insert(0, reject.name)

    def back_to_home_page_button_clicked(self):
        self.view.switch("home")
        self.counter = 1
        self.firstname_entry.delete(0, END)
        self.lastname_entry.delete(0, END)
        self.birthday_entry.delete(0, END)
        self.photo_label.config(image="")
        self.gender_entry.delete(0, END)
        self.skill_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.status_entry.delete(0, END)
