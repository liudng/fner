import os
import sys
from tkinter import Tk, Frame, Canvas
from PIL import Image, ImageTk
import subprocess
import values

def measure_screen():
    subprocess.call(['xrandr | grep \'*\' > /tmp/fner_tmp'], shell=True)
    resolution_string = open(values.tmp, 'r').read()
    # Workaround for possible crash when xrandr won't return "*"
    if not resolution_string:
        os.system('xrandr | grep \'+ \' > /tmp/fner_tmp')
        resolution_string = open(values.tmp, 'r').read()
    os.remove(values.tmp)

    resolution = resolution_string.split()[0]
    width, height = resolution.split('x')

    return int(width), int(height), float(int(width) / 1920)


def check_dimensions():
    # Get screen width, height and graphics scaling factor (as a percentage of full hd screen width)
    values.screen_dimensions = measure_screen()
    values.screen_width = values.screen_dimensions[0]
    values.screen_height = values.screen_dimensions[1]
    values.hud_side = int(values.screen_dimensions[0] * 0.13)  # HUD window side in pixels
    values.hud_scale = values.screen_dimensions[2]
    values.hud_margin_v = int(values.screen_height * 0.13)  # HUD vertical margin in pixels

    # Create the window geometry, e.g. "300x150+50+50"
    values.hud_geometry = str(values.hud_side) + "x" + str(values.hud_side) + "+" + str(
        int(values.screen_width / 2 - values.hud_side / 2)) + "+" + str(
        values.screen_height - values.hud_side - values.hud_margin_v)


class Hud(Tk):

    def __init__(self, icon, message):
        super().__init__()
        self.geometry(values.hud_geometry)
        self.frame = Frame(self)
        self.frame.pack()

        self.canvas = Canvas(self.frame)
        self.canvas.pack()

        self.overrideredirect(1)

        image = Image.open(icon)
        image = image.resize((values.hud_side, values.hud_side), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(image)

        self.canvas.create_image(values.hud_side / 2, values.hud_side / 2, image=self.img)
        self.canvas.create_text(values.hud_side / 2, int(190 * values.hud_scale),
                                font="Helvetica" + str(int(14 * values.hud_scale)),
                                text=message, fill='gray')

def show_hud(icon, message, timeout):
    hud = Hud("icons/" + icon + ".png", message)
    hud.after(timeout, lambda: hud.destroy())
    hud.mainloop()


def volume(command):
    if command == "up":
        os.system(values.volume_up)
    elif command == "down":
        os.system(values.volume_down)
    elif command == "toggle":
        os.system(values.volume_toggle)

    os.system(values.volume_get_level)
    volume_lvl = open(values.tmp, 'r').read()
    os.remove(values.tmp)
    volume_lvl = volume_lvl.split("%")[0]

    volume_int = int(round(float(volume_lvl.rstrip())))
    if volume_int == 100:
        volume_icon = "volume-high"
    elif volume_int >= 50:
        volume_icon = "volume-medium"
    elif volume_int > 0:
        volume_icon = "volume-low"
    else:
        volume_icon = "volume-zero"

    if command != "toggle":

        show_hud(volume_icon, volume_lvl + "%", 1000)

    else:
        os.system(values.volume_get_status)
        volume_status = open(values.tmp, 'r').read()
        volume_status = volume_status.rstrip()
        os.remove(values.tmp)

        if volume_status == "off":
            show_hud("volume-muted", "Muted", 1000)
        else:
            show_hud(volume_icon, volume_lvl + "%", 1000)


def brightness(command):
    # We will use the optional light-git package if installed or xbacklight if not
    if command == "up":
        os.system(values.brightness_up)
    elif command == "down":
        os.system(values.brightness_down)

    os.system(values.brightness_get_level)

    brightness_lvl = open(values.tmp, 'r').read()
    os.remove(values.tmp)

    brightness_int = 0
    try:
        brightness_int = int(round(float(brightness_lvl.rstrip())))
        brightness_str = str(brightness_int) + "%"
    except ValueError:
        brightness_str = "xbacklight?"

    if brightness_int == 100:
        brightness_icon = "brightness-full"
    elif brightness_int > 60:
        brightness_icon = "brightness-high"
    elif brightness_int >= 40:
        brightness_icon = "brightness-medium"
    elif brightness_int > 0:
        brightness_icon = "brightness-low"
    else:
        brightness_icon = "brightness-medium"

    show_hud(brightness_icon, brightness_str, 1000)


def main():
    # values.tmp = "/tmp/fner_tmp".rstrip()

    check_dimensions()

    if sys.argv[1] == "--volume":
        if sys.argv[2] == "up" or sys.argv[2] == "down" or sys.argv[2] == "toggle":
            volume(sys.argv[2])
        else:
            print("Unknown command \'" + sys.argv[2] + "\'")

    elif sys.argv[1] == "--brightness":
        if sys.argv[2] == "up" or sys.argv[2] == "down":
            brightness(sys.argv[2])
        else:
            print("Unknown command \'" + sys.argv[2] + "\'")

if __name__ == "__main__":
    main()
