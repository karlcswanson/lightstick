import mido


KEYBOARD = []

inport = mido.open_input('MPKmini2:MPKmini2 MIDI 1 20:0')

class note:
    def __init__(self, note):
        self.note = note
        self.velocity = 0

    def note_on(self, velocity):
        self.velocity = velocity
        # if self.note < 25:
        #     dots[self.note] = color()

    def note_off(self):
        self.velocity = 0
        # if self.note < 25:
        #     dots[self.note] = (0, 0, 0)

    def __repr__(self):
        return 'note: {} velocity: {}'.format(self.note, self.velocity)


def keyboard_init():
    for i in range (0, 87):
        KEYBOARD.append(note(i))
    print(KEYBOARD)

    # n_dots = len(dots)
    # for dot in range(n_dots):
    #     dots[dot] = ( 0, 0, 0)

    # time.sleep(.25)
    # print(dots)

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
