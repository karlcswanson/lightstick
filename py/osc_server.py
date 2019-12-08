import config

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer


def preset_handler(address, *args):
    print("Preset: {}".format(args[0]))
    preset = int(args[0])

    if config.get_preset_by_number(preset):
        config.config_tree['current_preset'] = preset
        config.save_current_config()


def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")


def osc_server():
    dispatcher = Dispatcher()
    dispatcher.map("/lightstick/preset", preset_handler)
    dispatcher.set_default_handler(default_handler)

    ip = "0.0.0.0"
    port = 5000

    server = BlockingOSCUDPServer((ip, port), dispatcher)
    server.serve_forever()