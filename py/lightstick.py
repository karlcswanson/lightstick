import threading


import midi
import config
import tornado_server
import led

def main():
    config.config()
    midi.keyboard_init()
    led.led_init()
    print(config.config_tree)

    web_t = threading.Thread(target=tornado_server.twisted)
    midi_t = threading.Thread(target=midi.midi_loop)
    led_t = threading.Thread(target=led.led_loop)

    web_t.start()
    midi_t.start()
    led_t.start()

if __name__ == '__main__':
    main()