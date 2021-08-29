from tkinter import *
from PIL import ImageTk, Image
from music_player import music_controller
from mutagen.mp3 import MP3


class switch:
    def __init__(self, root, dis_obj):
        self.root = root
        self.dis_obj = dis_obj
        self.menu_frame = Frame(self.root, bg="#333333", height=64)
        self.pause = ImageTk.PhotoImage(Image.open("images/pause.png"))
        self.resume = ImageTk.PhotoImage(Image.open("images/play.png"))
        self.next_left = ImageTk.PhotoImage(Image.open("images/next_left.png"))
        self.next_right = ImageTk.PhotoImage(Image.open("images/next_right.png"))
        self.p = Button(self.menu_frame, image=self.pause, bd=0, bg="#333333",
                        command=lambda: self.change_pause_btn())
        self.nl = Button(self.menu_frame, image=self.next_left, bd=0, bg="#333333", command=self.change_to_prev)
        self.nr = Button(self.menu_frame, image=self.next_right, bd=0, bg="#333333", command=self.change_to_next)
        self.res = Button(self.menu_frame, image=self.resume, bd=0, bg="#333333",
                          command=lambda: self.change_resume_btn())

        self.slider_value = DoubleVar()
        self.slider = None

    def create_menu(self):
        self.menu_frame.pack(side=BOTTOM, fill=BOTH)
        self.menu_frame.pack_propagate(0)
        self.nl.pack(side=LEFT, padx=60)
        self.res.pack(side=LEFT, padx=10)
        self.nr.pack(side=LEFT, padx=55)

    def change_pause_btn(self):
        self.p.pack_forget()
        self.nr.pack_forget()
        self.res.pack(side=LEFT, padx=10)
        self.nr.pack(side=LEFT, padx=55)
        # here comes the code to play music
        music_controller.music_pause(self.dis_obj)

    def change_resume_btn(self):
        self.res.pack_forget()
        self.nr.pack_forget()
        self.p.pack(side=LEFT, padx=10)
        self.nr.pack(side=LEFT, padx=55)
        # here comes the code to play music
        if not music_controller.active_music:
            music_controller.active_music = music_controller.music_array[0]
            music_controller.load_music()
        self.dis_obj.set_image()
        flen = MP3(music_controller.path + "/" + music_controller.active_music)
        filLen = flen.info.length
        if music_controller.paused:
            if self.slider:
                self.slider.pack_forget()
            self.slider_value.set(0)
            self.create_scale(filLen)
        music_controller.music_play(self.slider_value, self.dis_obj, self)

    def change_to_prev(self):
        music_controller.music_index -= 1
        if music_controller.music_index < 0:
            music_controller.music_index = len(music_controller.music_array) - 1
        music_controller.active_music = music_controller.music_array[music_controller.music_index]
        music_controller.paused = True
        music_controller.load_music()
        self.change_resume_btn()

    def change_to_next(self):
        music_controller.music_index += 1
        if music_controller.music_index > len(music_controller.music_array) - 1:
            music_controller.music_index = 0
        music_controller.active_music = music_controller.music_array[music_controller.music_index]
        music_controller.paused = True
        music_controller.load_music()
        self.change_resume_btn()

    def create_scale(self, filen):
        self.slider = Scale(self.dis_obj.display_frame, to=filen, orient=HORIZONTAL, width=7, length=365, resolution=0,
                            showvalue=False, digit=4, variable=self.slider_value, sliderrelief='flat',
                            highlightthickness=0, bg="red", fg="grey", troughcolor="#73B5FA", activebackground="red",
                            bd=0, sliderlength=10, command=self.progress)
        self.slider.pack(side=BOTTOM)

    def progress(self, value):
        music_controller.Progressbar(value, self.slider_value, self.dis_obj, self)
