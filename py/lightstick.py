import threading


import midi
import config
import tornado_server

def main():
    config.config()
    midi.keyboard_init()
    print(config.config_tree)

    web_t = threading.Thread(target=tornado_server.twisted)
    midi_t = threading.Thread(target=midi.midi_loop)

    web_t.start()
    midi_t.start()

if __name__ == '__main__':
    main()