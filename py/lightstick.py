import mido

KEYBOARD = []


class note:
    def __init__(self, note):
        self.note = note
        self.velocity = 0

    def note_on(self, velocity):
        self.velocity = velocity

    def note_off(self):
        self.velocity = 0

    def __repr__(self):
        return 'note: {} velocity: {}'.format(self.note, self.velocity)


def keyboard_init():
    for i in range (0, 87):
        KEYBOARD.append(note(i))
    print(KEYBOARD)

def main():
    keyboard_init()
    inport = mido.open_input()
    while True:
        msg = inport.receive()
        if msg.type in ['note_on', 'note_off']:
            note = KEYBOARD[msg.note]

            if msg.type == 'note_on':
                note.note_on(msg.velocity)

            if msg.type == 'note_off':
                note.note_off()


            print(KEYBOARD[msg.note])
        # print('{}'.format(msg))

if __name__ == '__main__':
    main()
