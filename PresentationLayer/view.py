from .window import Window
from .main_page import MainPage
from .create_resumes import Resumes
from .login_for_admin import LoginAdmin
from .home import HomeFrame
from .show_resumes import ShowResumesFrame
from .profile import ProfileFrame


class MainView:
    def __init__(self):
        self.window = Window()

        self.frames = {}

        self.add_frame("resumes", Resumes(self, self.window))
        self.add_frame("profile", ProfileFrame(self, self.window))
        self.add_frame("show_resumes", ShowResumesFrame(self, self.window))
        self.add_frame("home", HomeFrame(self, self.window))
        self.add_frame("login", LoginAdmin(self, self.window))
        self.add_frame("main_page", MainPage(self, self.window))

        self.window.show()

    def add_frame(self, frame_name, frame):
        self.frames[frame_name] = frame
        self.frames[frame_name].grid(row=0, column=0, sticky="nsew")

    def switch(self, frame_name):
        self.frames[frame_name].tkraise()
        return self.frames[frame_name]
