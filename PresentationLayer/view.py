from .window import Window


class MainView:
    def __init__(self):
        self.frames = {}

        self.window = Window()

        self.window.show()

    def add_frame(self, frame_name, frame):
        self.frames[frame_name] = frame
        self.frames[frame_name].grid(row=0, column=0, sticky="nsew")
