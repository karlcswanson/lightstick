import time
import random

import mido
import osc

import led

KEYBOARD = []

inport = mido.open_input('MPKmini2:MPKmini2 MIDI 1 20:0')


class note:
    def __init__(self, note):
        self.note = note
        self.velocity = 0
        self.timestamp = time.time()

    def note_on(self, velocity):
        self.velocity = velocity
        self.timestamp = time.time()


    def note_off(self):
        self.velocity = 0
        self.timestamp = time.time()


    def ratio(self, atk_rel_time):
        if atk_rel_time == 0:
            return 1

        out = (time.time() - self.timestamp)/atk_rel_time
        if out > 1:
            return 1
        return out

    def __repr__(self):
        return 'note: {} velocity: {}'.format(self.note, self.velocity)


def keyboard_init():
    # for i in range (0, 87):
    for i in range(0, 87):
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
            print(msg.bytes())
        
        
        # out = ( 1,)
        # out = out + tuple(msg.bytes())

        # out = bytes(out)
        # if isinstance(out, tuple) and len(out) == 4:
        #     print("is tupple")
        # print('output: {}'.format(out))
        # osc.server.send('/midi', out)