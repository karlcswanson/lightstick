import time
import random

import numpy
import board
import adafruit_dotstar as dotstar

import config
import midi

NOTE_OFF_COLOR = (0, 0, 1)
NOTE_ON_COLOR = (30, 30, 30)
ATTACK = 1.0
RELEASE = .5

dots = dotstar.DotStar(board.SCK, board.MOSI, 185, brightness=0.1, auto_write=False)
# dots = dotstar.DotStar(board.SCK, board.MOSI, 25)

def random_color():
    return random.randrange(0, 7) * 32

def color():
    return (random_color(), random_color(), random_color())


def led_init():
    n_dots = len(dots)
    for dot in range(n_dots):
        dots[dot] = (0, 0, 0)

    time.sleep(.25)
    print(dots)


def calc_color(starting_color, target_color, ratio):
    return numpy.int_(starting_color + ratio * numpy.subtract(target_color, starting_color))

def update_colors():
    preset = current_preset()
    for key in midi.KEYBOARD:
        dots[key.note] = color_output(key, preset)
    dots.show()

def color_output(key, preset):
    if key.velocity > 0:
        return calc_color(preset['note_off'], preset['note_on'], key.ratio(preset['attack']))
    if key.velocity == 0:
        return calc_color(preset['note_on'], preset['note_off'], key.ratio(preset['decay']))

def update_colors_new():
    preset = current_preset()
    start_led = config.config_tree['start_led']

    for i in range(0, 88):
        dots[(2*i) + start_led] = color_output(midi.KEYBOARD[i + 21], preset)
        dots[(2*i) + start_led + 1] = color_output(midi.KEYBOARD[i + 21], preset)
    dots.show()

def current_preset():
    preset_number = config.config_tree['current_preset']

    for preset in config.config_tree['presets']:
        if preset['preset'] == preset_number:
            return preset


def led_loop():
    while True:
        update_colors_new()
        time.sleep(.02)
