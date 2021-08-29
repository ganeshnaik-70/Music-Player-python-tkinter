from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from music_player import music_controller


class menu:
    def __init__(self, root, ml, aud_obj, dis_obj, s_obj):
        self.root = root
        self.list_obj = ml
        self.audio_obj = aud_obj
        self.dis_obj = dis_obj
        self.s_obj = s_obj
        self.menu_frame = Frame(self.root, bg="#2e3233", height=64)
        self.menu_img = ImageTk.PhotoImage(Image.open("images/menu (1).png"))
        self.menu_btn = Button(self.menu_frame, image=self.menu_img, bd=0, relief=FLAT, bg="#2e3233",
                               command=self.delete_music_list)
        self.menu_active = True
        self.b = Button(self.list_obj.main_frame, text="Select music path", width=40, font=("Verdana", 13), anchor=W,
                        bd=1, relief=RIDGE, bg="#565051", fg="white", command=self.get_path)
        self.bg = Button(self.list_obj.main_frame, text="Select Background Image", width=40, font=("Verdana", 13),
                         anchor=W, bd=1, relief=RIDGE, bg="#565051", fg="white", command=self.display_background)

    def create_menu(self):
        self.menu_frame.pack(side=TOP, fill=BOTH)
        self.menu_frame.pack_propagate(0)
        self.menu_btn.pack(side=LEFT, anchor=S, padx=10, pady=10)

    def delete_music_list(self):
        if self.menu_active:
            self.list_obj.sb.pack_forget()
            self.s_obj.p.configure(state=DISABLED)
            self.s_obj.res.configure(state=DISABLED)
            self.s_obj.nl.configure(state=DISABLED)
            self.s_obj.nr.configure(state=DISABLED)
            for child in self.list_obj.main_frame.winfo_children():
                child.pack_forget()
            self.b.pack(side=TOP)
            self.bg.pack(side=TOP)
            self.list_obj.main_frame.configure(bg="#565051")
            self.menu_active = False
        else:
            self.list_obj.sb.pack(side=RIGHT, fill=Y)
            self.s_obj.p.configure(state=NORMAL)
            self.s_obj.res.configure(state=NORMAL)
            self.s_obj.nl.configure(state=NORMAL)
            self.s_obj.nr.configure(state=NORMAL)
            for label in self.list_obj.m_list:
                label.pack(side=TOP, pady=1, anchor=W)
            for child in self.dis_obj.display_frame.winfo_children():
                if child.winfo_class() == "Button" or child.winfo_class() == "Label":
                    if child != self.dis_obj.b:
                        child.grid_forget()
            self.dis_obj.b.pack()
            self.b.pack_forget()
            self.bg.pack_forget()
            self.list_obj.main_frame.configure(bg="#343d52")
            self.menu_active = True

    def get_path(self):
        path = filedialog.askdirectory()
        if path:
            self.delete_music_list()
            self.list_obj.show_list()
            self.audio_obj.d = path
        music_controller.set_path(self.audio_obj.d)
        self.list_obj.m_list.clear()
        self.audio_obj.music_name.clear()
        self.audio_obj.get_files(self.list_obj)

    def display_background(self):
        self.dis_obj.display_background()
