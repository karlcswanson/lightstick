import time
import random

import mido

import led

KEYBOARD = []

inport = mido.open_input('MPKmini2:MPKmini2 MIDI 1 20:0')

NOTE_ON_COLOR = ( 147, 112, 219)
ATTACK = 0.5
RELEASE = 1.0
NOTE_OFF_COLOR = ( 255, 20, 147)

class note:
    def __init__(self, note):
        self.note = note
        self.velocity = 0
        
        self.target_brightness = 0
        self.timestamp = time.time()

    def note_on(self, velocity):
        self.velocity = velocity
        self.target_brightness = velocity * 2
        if self.note < 25:
            led.dots[self.note] = (255, 0, 0, random.random())

    def note_off(self):
        self.velocity = 0
        # self.target_brightness
        if self.note < 25:
            led.dots[self.note] = (0, 0, 0)

    def __repr__(self):
        return 'note: {} velocity: {}'.format(self.note, self.velocity)


def keyboard_init():
    for i in range (0, 87):
        KEYBOARD.append(note(i))
    print(KEYBOARD)

    

def midi_loop():  
    while True:
        msg = inport.receive()
        if msg.type in ['note_on', 'note_off']:
            note = KEYBOARD[msg.note]

            if msg.type == 'note_on':
                note.note_on(msg.velocity)

            if msg.type == 'note_off':
                note.note_off()

            print(KEYBOARD[msg.note])
