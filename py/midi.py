import time
import random

import mido
import osc

import led

KEYBOARD = []

SUSTAIN = []

inport = mido.open_input('MPKmini2:MPKmini2 MIDI 1 20:0')

class midiControlChange:
    def __init__(self, control_number):
        self.control_value = 0
        self.control_number = control_number
        self.timestamp = time.time()
    
    def set_val(self, control_value):
        self.control_value = control_value
        self.timestamp = time.time()

class sustain(midiControlChange):
    def __init__(self):
        super().__init__(64)
        self.note_hold_list = []

    def hold_note_off(self,note):
        self.note_hold_list.append(note)

    def release_notes(self):
        for note in self.note_hold_list:
            note.note_off()
        del self.note_hold_list[:]

    def set_val(self, control_value):
        self.control_value = control_value
        self.timestamp = time.time()

        if control_value == 0:
            self.release_notes()
    
    def pedal_state(self):
        if (self.control_value == 127):
            return 'PRESSED'
        return 'RELEASED'



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
    global SUSTAIN
    # for i in range (0, 87):
    for i in range(0, 88):
        KEYBOARD.append(note(i))
    
    SUSTAIN = sustain()
    print(KEYBOARD)



def midi_loop():
    while True:
        msg = inport.receive()
        # print(msg)
        if msg.type == 'control_change':
            if msg.control == 64:
                SUSTAIN.set_val(msg.value)
                print("Sustain: {}".format(SUSTAIN.control_value))

        if msg.type in ['note_on', 'note_off']:
            if msg.note < 88:
                note = KEYBOARD[msg.note]

                if msg.type == 'note_on':
                    note.note_on(msg.velocity)

                if msg.type == 'note_off':
                    if (SUSTAIN.pedal_state() == 'PRESSED'):
                        SUSTAIN.hold_note_off(note)
                    else:
                        note.note_off()

                print(KEYBOARD[msg.note])
                print(msg.bytes())