import threading


import midi
import config
import tornado_server
import led
import osc
import osc_server

def main():
    config.config()
    midi.keyboard_init()
    led.led_init()
    osc.OSCInit()
    print(config.config_tree)

    web_t = threading.Thread(target=tornado_server.twisted)
    midi_t = threading.Thread(target=midi.midi_loop)
    led_t = threading.Thread(target=led.led_loop)
    osc_t = threading.Thread(target=osc.osc_loop)
    osc_server_t = threading.Thread(target=osc_server.osc_server)

    web_t.start()
    midi_t.start()
    led_t.start()
    osc_t.start()
    osc_server_t.start()

if __name__ == '__main__':
    main()