import time
import random

import numpy
import board
import adafruit_dotstar as dotstar

import config
import midi


dots = dotstar.DotStar(board.SCK, board.MOSI, 185, brightness=0.5, auto_write=False)


def led_init():
    n_dots = len(dots)
    for dot in range(n_dots):
        dots[dot] = (0, 0, 0)

    time.sleep(.25)
    print(dots)


def calc_color(starting_color, target_color, ratio):
    return numpy.int_(starting_color + ratio * numpy.subtract(target_color, starting_color))


def color_output(key, preset):
    if key.velocity > 0:
        return calc_color(preset['note_off'], preset['note_on'], key.ratio(preset['attack']))
    if key.velocity == 0:
        return calc_color(preset['note_on'], preset['note_off'], key.ratio(preset['decay']))

def update_colors():
    preset = current_preset()
    start_led = config.config_tree['start_led']

    for i in range(0, 88):
        try:
            dots[(2*i) + start_led] = color_output(midi.KEYBOARD[i + 21], preset)
            dots[(2*i) + start_led + 1] = color_output(midi.KEYBOARD[i + 21], preset)
        except:
            print('OH No 2.0')
    try:
        dots.show()
    except:
        print('0hno 3.0')


def current_preset():
    preset_number = config.config_tree['current_preset']

    for preset in config.config_tree['presets']:
        if preset['preset'] == preset_number:
            return preset


def led_loop():
    while True:
        update_colors()
        time.sleep(.02)
