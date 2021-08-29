from pygame import mixer
import stagger
import io
import warnings

warnings.filterwarnings("ignore")
music_array = []
music_index = 0
path = ''
paused = True
active_music = ""
mp3 = ""
bg_img = "images/background/bg5.jpg"
im = "images/background/bg5.jpg"
by_data = ''
playtime = ""
loopID = ""


def set_path(p):
    global path
    path = p


def set_active_music(music_name):
    global active_music, music_index
    active_music = music_name
    music_index = set_index()


def load_music():
    global mp3, by_data, im
    mixer.init()
    mixer.music.load(path + "/" + active_music)
    try:
        mp3 = stagger.read_tag(path + "/" + active_music)
        by_data = mp3[stagger.id3.APIC][0].data
        im = io.BytesIO(by_data)
    except:
        im = get_image()


def set_index():
    return music_array.index(active_music)


def music_play(slider_value, dis_obj, s_obj):
    global paused, playtime
    playtime = 0
    if paused:
        if loopID:
            dis_obj.display_frame.after_cancel(loopID)
        playtime = slider_value.get()
        mixer.music.play(start=playtime)
        TrackPlay(playtime, slider_value, dis_obj, s_obj)
    else:
        playtime = slider_value.get()
        mixer.music.play(start=playtime)
        TrackPlay(playtime, slider_value, dis_obj, s_obj)


def TrackPlay(p, slider_value, dis_obj, s_obj):
    global loopID
    if mixer.music.get_busy():
        slider_value.set(p)
        p += 1.0
        loopID = dis_obj.display_frame.after(1000, lambda: TrackPlay(p, slider_value, dis_obj, s_obj))
    else:
        s_obj.change_to_next()
        s_obj.change_pause_btn()


def Progressbar(value, slider_value, dis_obj, s_obj):
    if mixer.music.get_busy():
        dis_obj.display_frame.after_cancel(loopID)  # Move slider to new position
        slider_value.set(value)
        music_play(slider_value, dis_obj, s_obj)
    else:
        slider_value.set(value)


def music_pause(dis_obj):
    global paused
    mixer.music.stop()
    dis_obj.display_frame.after_cancel(loopID)
    paused = False


def get_image():
    global im
    im = bg_img
    return im
