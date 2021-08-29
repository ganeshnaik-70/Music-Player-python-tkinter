from tkinter import *
import os
from music_player import music_controller
from tkinter import filedialog
from tkinter import messagebox


class audio:
    def __init__(self):
        self.d = ""
        while self.d == "":
            self.d = filedialog.askdirectory()
            if self.d == "":
                messagebox.askretrycancel(title="Select the Music folder",
                                          message="Please select a folder where your music file is")

        music_controller.set_path(self.d)
        self.files = os.listdir(self.d)
        self.music_name = []

    def get_files(self, obj):
        if self.d == "":
            self.d = filedialog.askdirectory()
        self.files = os.listdir(self.d)
        for file in self.files:
            if file.endswith(".mp3"):
                obj.add_music_list(file)
                self.music_name.append(file)
        music_controller.music_array = self.music_name


class music_menu:
    def __init__(self, root, switch_obj):
        self.root = root
        self.music_frame = Frame(self.root, bg="#343d52", height=457)
        self.my_canvas = Canvas(self.music_frame, width=289)
        self.sb = Scrollbar(self.music_frame, orient=VERTICAL, command=self.my_canvas.yview)
        self.main_frame = Frame(self.my_canvas, bg="#343d52", width=290, height=455)
        self.m_list = []
        self.height = 0
        self.active_music = ""
        self.switch_obj = switch_obj

    def create_menu(self):
        self.music_frame.pack(side=BOTTOM, fill=BOTH, expand=1)
        self.my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.sb.pack(side=RIGHT, fill=Y)
        self.my_canvas.configure(yscrollcommand=self.sb.set)
        self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))
        self.my_canvas.create_window((0, 0), window=self.main_frame, anchor="nw")
        # for mouse scroll
        self.my_canvas.bind_all('<MouseWheel>', self.on_mouse_wheel)
        self.main_frame.pack_propagate(0)

    # this method is used to scroll the frame using mouse
    def on_mouse_wheel(self, event):
        self.my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

    def add_music_list(self, file):
        ml = Button(self.main_frame, text=file, width=41, bd=1, relief=RIDGE, fg="white", bg="#343d52", pady=6,
                    anchor=W, command=lambda: self.set_active(file))
        self.m_list.append(ml)

    def show_list(self):
        for label in self.m_list:
            label.pack(side=TOP, pady=1, anchor=W)

        # this is to adjust the height of the frame based on no of audio files
        self.height = len(self.m_list) * 36
        if self.height > 455:
            self.main_frame.configure(height=self.height)

    def set_active(self, music_name):
        music_controller.set_active_music(music_name)
        music_controller.paused = True
        music_controller.load_music()
        self.switch_obj.change_resume_btn()
