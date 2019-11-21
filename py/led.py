import time
import random

import board
import adafruit_dotstar as dotstar

dots = dotstar.DotStar(board.SCK, board.MOSI, 25, brightness=1)



def random_color():
    return random.randrange(0, 7) * 32

def color():
    return (random_color(), random_color(), random_color())


class LED:
    def __init__(self)
