import os
import sys
import json
import logging
import logging.handlers
import argparse

APPNAME = 'lightstick'

CONFIG_FILE_NAME = 'config.json'

FORMAT = '%(asctime)s %(levelname)s:%(message)s'

config_tree = {}
args = {}

def logging_init():
    formatter = logging.Formatter(FORMAT)
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    sthandler = logging.StreamHandler(sys.stdout)
    fhandler = logging.handlers.RotatingFileHandler(log_file(),
                                                    maxBytes=10*1024*1024,
                                                    backupCount=5)

    sthandler.setFormatter(formatter)
    fhandler.setFormatter(formatter)

    log.addHandler(sthandler)
    log.addHandler(fhandler)


def web_port():
    if args['server_port'] is not None:
        return int(args['server_port'])

    elif 'LIGHTSTICK_PORT' in os.environ:
        return int(os.environ['LIGHTSTICK_PORT'])

    return config_tree['port']


def os_config_path():
    path = os.getcwd()
    if sys.platform.startswith('linux'):
        path = os.getenv('XDG_DATA_HOME', os.path.expanduser("~/.local/share"))
    elif sys.platform == 'win32':
        path = os.getenv('LOCALAPPDATA')
    elif sys.platform == 'darwin':
        path = os.path.expanduser('~/Library/Application Support/')
    return path


def config_path(folder=None):
    if args['config_path'] is not None:
        if os.path.exists(os.path.expanduser(args['config_path'])):
            path = os.path.expanduser(args['config_path'])
        else:
            logging.warning("Invalid config path")
            sys.exit()

    else:
        path = os.path.join(os_config_path(), APPNAME)
        if not os.path.exists(path):
            os.makedirs(path)

    if folder:
        return os.path.join(path, folder)
    return path

def log_file():
    return config_path('lightstick.log')

# https://stackoverflow.com/questions/404744/determining-application-path-in-a-python-exe-generated-by-pyinstaller
def app_dir(folder=None):
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
        return os.path.join(application_path, folder)

    if __file__:
        application_path = os.path.dirname(__file__)

    return os.path.join(os.path.dirname(application_path), folder)


def config_file():
    if os.path.exists(app_dir(CONFIG_FILE_NAME)):
        return app_dir(CONFIG_FILE_NAME)
    elif os.path.exists(config_path(CONFIG_FILE_NAME)):
        return config_path(CONFIG_FILE_NAME)
    else:
        logging.warning('No config file found!')
        sys.exit()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--config-path', help='configuration directory')
    parser.add_argument('-p', '--server-port', help='server port')
    args,_ = parser.parse_known_args()

    return vars(args)


def config():
    global args
    args = parse_args()
    logging_init()
    read_json_config(config_file())
    logging.info('Starting lightstick {}'.format(config_tree['lightstick_version']))


def get_version_number():
    with open(app_dir('package.json')) as package:
        pkginfo = json.load(package)

    return pkginfo['version']

def read_json_config(file):
    global config_tree
    with open(file) as config_file:
        config_tree = json.load(config_file)

    config_tree['lightstick_version'] = get_version_number()


def write_json_config(data):
    with open(config_file(), 'w') as f:
        json.dump(data, f, indent=2, separators=(',', ': '), sort_keys=True)

def save_current_config():
    return write_json_config(config_tree)


def get_preset_by_number(preset_number):
    for preset in config_tree['presets']:
        if preset['preset'] == int(preset_number):
            return preset
    return None

def update_preset(data):
    preset = get_preset_by_number(data['preset'])
    

    preset['title'] = data['title']
    preset['attack'] = float(data['attack'])
    preset['decay'] = float(data['decay'])
    preset['note_off'] = data['note_off']
    preset['note_on'] = data['note_on']

    save_current_config()

def preset_select(data):
    preset = int(data['current_preset'])

    if get_preset_by_number(preset):
        config_tree['current_preset'] = preset
        save_current_config()
