import time

import logging
from pythonosc import udp_client

import config
import midi

server = []

OSCOutputQueue = []


def add_note_to_queue(midi_note):
    pass

def OSCInit():
    global server
    server = OSCConnection(config.config_tree['osc_server'], config.config_tree['osc_port'])

class OSCConnection:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = udp_client.SimpleUDPClient(self.host, self.port)

        try:
            self.s.send_message('/login/', 'Now Connected')
        except:
            logging.warning('Connection Error')

    def send(self, path, value):
        # logging.debug('sending {} to: {}:{}{}'.format(value, server.host, server.port, path))

        try:
            self.s.send_message(path, value)
        except:
            logging.warning(' Error sending {} to: {}:{}{}'.format(value, server.host, server.port, path))

def update_osc():
    for key in midi.KEYBOARD:
        server.send('/d3/layer/{}/brightness'.format(key.note + 1), key.velocity*2)


def osc_loop():
    while True:
        update_osc()
        time.sleep(.01)
