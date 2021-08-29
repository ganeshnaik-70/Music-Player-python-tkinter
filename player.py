from tkinter import *
from music_player.menu_frame import menu
from music_player.music_list import music_menu, audio
from music_player.music_switch import switch
from music_player.music_display import display
from tkinter import messagebox
from music_player import music_controller
from PIL import ImageTk, Image

root = Tk()
root.geometry("660x520+300+100")
# set the title of the window
root.title("Music Player")
# initialize and load icon for root window
icon = ImageTk.PhotoImage(Image.open("images/music-notes.png"))
root.iconphoto(False, icon)

left_frame = Frame(root, width=289)
left_frame.pack(side=LEFT, fill=BOTH)

right_frame = Frame(root)
right_frame.pack(side=RIGHT, fill=BOTH)

md = display(right_frame)
md.create_menu()
md.default_image()

s = switch(right_frame, md)
s.create_menu()

ml = music_menu(left_frame, s)
ml.create_menu()
a = audio()
a.get_files(ml)
ml.show_list()

m = menu(left_frame, ml, a, md, s)
m.create_menu()


def ask_quit():
    """Confirmation to quit application."""
    if messagebox.askokcancel("Quit", "Exit MusicPlayer"):
        music_controller.mixer.quit()
        root.destroy()


root.protocol("WM_DELETE_WINDOW", ask_quit)  # Tell Tk window instance what to do before it is destroyed.
root.mainloop()
