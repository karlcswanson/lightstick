import logging
from pythonosc import udp_client

server = []

OSCOutputQueue = []


def add_note_to_queue(midi_note):
    pass

def OSCInit():
    global server
    server = OSCConnection('karls-mbp.local', 8000)

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
        logging.debug('sending {} to: {}:{}{}'.format(value, server.host, server.port, path))

        try:
            self.s.send_message(path, value)
        except:
            logging.warning(' Error sending {} to: {}:{}{}'.format(value, server.host, server.port, path))