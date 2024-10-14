from tkinter import Frame, LabelFrame, Label, Button, Entry, Canvas, Radiobutton, IntVar, messagebox, END
from tkcalendar import DateEntry
from tkinter.font import Font
from tkinter.filedialog import askopenfilename
from datetime import date
from PIL import Image, ImageTk
from BusinessLogicLayer.form_business import FormBusiness


class Resumes(Frame):
    def __init__(self, view, window):
        super().__init__(window)

        self.form_business = FormBusiness()

        self.view = view

        self.filename = None
        self.image_data = None
        self.show_photo_tk = None

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

        self.font_entry = Font(family="Serif", size=12, weight="bold")

        self.header = LabelFrame(self.canvas, text="Form", borderwidth=0, background="#F39F5A", foreground="#31363F",
                                 labelanchor="n", font=self.font)
        self.header.grid_columnconfigure(1, weight=1)
        self.header.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), ipadx=500, ipady=200)

        # First Name
        self.firstname_label = Label(self.header, text="First Name :", background="#F39F5A", foreground="#31363F",
                                     font=self.font_label)
        self.firstname_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="w")

        self.firstname_entry = Entry(self.header, borderwidth=2, background="#EAD7BB", font=self.font_entry)
        self.firstname_entry.grid(row=0, column=1, padx=(0, 10), pady=(10, 10), sticky="ew")

        # Last Name
        self.lastname_label = Label(self.header, text="Last Name :", background="#F39F5A", foreground="#31363F",
                                    font=self.font_label)
        self.lastname_label.grid(row=1, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.lastname_entry = Entry(self.header, borderwidth=2, background="#EAD7BB", font=self.font_entry)
        self.lastname_entry.grid(row=1, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Birthday
        self.birthday_label = Label(self.header, text="Birthday :", background="#F39F5A", foreground="#31363F",
                                    font=self.font_label)
        self.birthday_label.grid(row=2, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.birthday_entry = DateEntry(self.header, date_pattern="yyyy-mm-dd", font=self.font_entry)
        self.birthday_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Gender
        self.gender_label = Label(self.header, text="Gender :", background="#F39F5A", foreground="#31363F",
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
        self.skill_label = Label(self.header, text="Skills :", background="#F39F5A", foreground="#31363F",
                                 font=self.font_label)
        self.skill_label.grid(row=4, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.skill_entry = Entry(self.header, borderwidth=2, background="#EAD7BB", font=self.font_entry)
        self.skill_entry.grid(row=4, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Email
        self.email_label = Label(self.header, text="Email :", background="#F39F5A", foreground="#31363F",
                                 font=self.font_label)
        self.email_label.grid(row=5, column=0, padx=(10, 10), pady=(0, 10), sticky="w")

        self.email_entry = Entry(self.header, borderwidth=2, background="#EAD7BB", font=self.font_entry)
        self.email_entry.grid(row=5, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")

        # Photo
        self.image_photo_button_tk = ImageTk.PhotoImage(
            Image.open("Images/1375106.png").resize(size=(100, 100)))

        self.photo_label = Label(self.header, background="#F39F5A")
        self.photo_label.grid(row=8, column=1, padx=(0, 10), pady=(50, 10))

        self.photo_button = Button(self.header, image=str(self.image_photo_button_tk), borderwidth=0,
                                   background="#F39F5A", text="Choose your photo", compound="top", font=self.font_label,
                                   command=self.photo_button_clicked, foreground="#31363F", activebackground="#F39F5A")
        self.photo_button.grid(row=6, column=1, padx=(0, 10), pady=(0, 10))

        # Save Button
        self.image_save_button_tk = ImageTk.PhotoImage(
            Image.open("Images/floppy-disk_2344287.png").resize(size=(100, 100)))

        self.save_button = Button(self.header, image=str(self.image_save_button_tk), background="#F39F5A",
                                  borderwidth=0, text="Save", compound="top", font=self.font_label, pady=10,
                                  foreground="#31363F", command=self.save_button_clicked, activebackground="#F39F5A")
        self.save_button.grid(row=7, column=1, padx=(0, 10), pady=(0, 10), sticky="w")

        # Back
        self.image_back_button_tk = ImageTk.PhotoImage(
            Image.open("Images/rewind_5542199.png").resize(size=(100, 100)))

        self.back = Button(self.header, text="Back", command=self.back_button_clicked, borderwidth=0,
                           image=str(self.image_back_button_tk), background="#F39F5A", compound="top",
                           font=self.font_label, pady=10, foreground="#31363F", activebackground="#F39F5A")
        self.back.grid(row=7, column=1, padx=(0, 50), pady=(0, 10), sticky="e")

    def size(self, event):
        self.image = Image.open("Images/black-abstract-dark-3840x2160-9729.jpg")
        self.image_resize = self.image.resize(size=(event.width, event.height))
        self.image_tk = ImageTk.PhotoImage(self.image_resize)
        self.canvas.create_image(0, 0, image=self.image_tk, anchor="nw")

    def photo_button_clicked(self):
        file_type = [("Png & Jpg Files", "*png;*jpg")]
        self.filename = askopenfilename(filetypes=file_type)
        if self.filename:
            self.show_photo_tk = ImageTk.PhotoImage(Image.open(self.filename).resize(size=(200, 200)))
            self.photo_label.config(image=str(self.show_photo_tk), background="#F39F5A")
        else:
            self.filename = None

    def save_button_clicked(self):
        firstname = self.firstname_entry.get()
        lastname = self.lastname_entry.get()
        birthday = self.birthday_entry.get()
        gender = self.gender_radio_button_var.get()
        skills = self.skill_entry.get()
        email = self.email_entry.get()

        if self.filename:
            with open(self.filename, mode="rb") as image:
                self.image_data = image.read()
        else:
            pass

        result = self.form_business.get_form(firstname, lastname, birthday, gender, skills, email, self.image_data)
        save_message = result[0]
        error_message = result[1]

        if error_message:
            messagebox.showerror(title="Error", message=error_message)
        else:
            messagebox.showinfo(title="Info", message=save_message)
            self.firstname_entry.delete(0, END)
            self.lastname_entry.delete(0, END)
            self.skill_entry.delete(0, END)
            self.email_entry.delete(0, END)
            self.photo_label.config(image="")

    def back_button_clicked(self):
        self.view.switch("main_page")
        self.firstname_entry.delete(0, END)
        self.lastname_entry.delete(0, END)
        self.skill_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.photo_label.config(image="")
