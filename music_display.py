from tkinter import *
from music_player import music_controller
from PIL import ImageTk, Image


class display:
    def __init__(self, root):
        self.root = root
        self.display_frame = Frame(self.root, bg="black", width=370, height=457)
        self.menu_img = None
        self.b = Label(self.display_frame, bd=0)
        self.img_array = []
        self.photoImage_array = []
        for i in range(1, 7):
            self.img_array.append("images/background/bg"+str(i)+".jpg")
        for i in self.img_array:
            img = Image.open(i)
            img = img.resize((120, 150), Image.ANTIALIAS)
            self.photoImage_array.append(ImageTk.PhotoImage(img))
        self.button_array = []
        for i in range(len(self.photoImage_array)):
            self.button_array.append(Button(self.display_frame, image=self.photoImage_array[i], relief=FLAT))
        self.button_array[0].configure(command=lambda: self.change_img(self.img_array[0]))
        self.button_array[1].configure(command=lambda: self.change_img(self.img_array[1]))
        self.button_array[2].configure(command=lambda: self.change_img(self.img_array[2]))
        self.button_array[3].configure(command=lambda: self.change_img(self.img_array[3]))
        self.button_array[4].configure(command=lambda: self.change_img(self.img_array[4]))
        self.button_array[5].configure(command=lambda: self.change_img(self.img_array[5]))
        """self.slider_value = DoubleVar()
        self.slider = Scale(self.display_frame, to=1000, orient=HORIZONTAL, width=7, length=365, resolution=0,
                       showvalue=False, digit=4, variable=self.slider_value, sliderrelief='flat', highlightthickness=0,
                       bg="red", fg="grey", troughcolor="#73B5FA", activebackground="red", bd=0,sliderlength=10)
        self.slider.pack(side=BOTTOM)"""

    def create_menu(self):
        self.display_frame.pack(side=TOP, fill=BOTH)
        self.display_frame.pack_propagate(0)

    def set_image(self):
        img = Image.open(music_controller.im)
        img = img.resize((360, 449), Image.ANTIALIAS)
        self.menu_img = ImageTk.PhotoImage(img)
        self.b.configure(image=self.menu_img)
        self.b.pack()

    def default_image(self):
        self.b.pack()
        img = Image.open("images/background/bg5.jpg")
        img = img.resize((360, 449), Image.ANTIALIAS)
        self.menu_img = ImageTk.PhotoImage(img)
        self.b.configure(image=self.menu_img)

    def display_background(self):
        self.b.pack_forget()
        self.button_array[0].grid(row=0, column=0)
        self.button_array[1].grid(row=0, column=1)
        self.button_array[2].grid(row=0, column=2)
        self.button_array[3].grid(row=1, column=0)
        self.button_array[4].grid(row=1, column=1)
        self.button_array[5].grid(row=1, column=2)
        for i in range(7):
            Label(self.display_frame, bg="black").grid(row=i+2, column=0)

    def change_img(self, img):
        music_controller.bg_img = img
        img = Image.open(music_controller.bg_img)
        img = img.resize((360, 449), Image.ANTIALIAS)
        self.menu_img = ImageTk.PhotoImage(img)
        self.b.configure(image=self.menu_img)
