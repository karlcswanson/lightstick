import time
import random

import numpy
import board
import adafruit_dotstar as dotstar
import midi

NOTE_OFF_COLOR = (0, 0, 1)
NOTE_ON_COLOR = (30, 30, 30)
ATTACK = 1.0
RELEASE = .5

dots = dotstar.DotStar(board.SCK, board.MOSI, 25, brightness=1)

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
    for key in midi.KEYBOARD:
        if key.velocity > 0:
            dots[key.note] = calc_color(NOTE_OFF_COLOR, NOTE_ON_COLOR, key.ratio(ATTACK))
        if key.velocity == 0:
            dots[key.note] = calc_color(NOTE_ON_COLOR, NOTE_OFF_COLOR, key.ratio(RELEASE))

def led_loop():
    while True:
        update_colors()
        time.sleep(.01)
