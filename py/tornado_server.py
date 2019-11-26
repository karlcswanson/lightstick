import json
import os
import asyncio
import socket
import logging

from tornado import websocket, web, ioloop, escape

import config


class IndexHandler(web.RequestHandler):
    def get(self):
        self.render(config.app_dir("index.html"))

class JsonHandler(web.RequestHandler):
    def get(self):
        
        json_out = json.dumps({
            'config': config.config_tree
        }, sort_keys=True, indent=4)


        self.set_header('Content-Type', 'application/json')
        self.write(json_out)

class PresetHandler(web.RequestHandler):
    def get(self):
        
        json_out = json.dumps({
            'presets': config.config_tree['presets']
        }, sort_keys=True, indent=4)


        self.set_header('Content-Type', 'application/json')
        self.write(json_out)
    
    def post(self):
        data = json.loads(self.request.body)
        config.update_preset(data)
        print(data)
        self.write(data)

class PresetChooser(web.RequestHandler):
    def get(self):
        self.write('hi')
    
    def post(self):
        data = json.loads(self.request.body)
        config.preset_select(data)
        print(data)
        self.write(data)

class SocketHandler(websocket.WebSocketHandler):
    clients = set()

    def check_origin(self, origin):
        return True

    def open(self):
        self.clients.add(self)

    def on_close(self):
        self.clients.remove(self)

    @classmethod
    def broadcast(cls, data):
        for c in cls.clients:
            try:
                c.write_message(data)
            except:
                logging.warning("WS Error")

    @classmethod
    def ws_dump(cls):
        out = {}

        if out:
            data = json.dumps(out)
            cls.broadcast(data)



def twisted():
    app = web.Application([
        (r'/', IndexHandler),
        # (r'/ws', SocketHandler),
        (r'/data', JsonHandler),
        (r'/api/preset', PresetHandler),
        (r'/api/preset_select', PresetChooser),
        (r'/static/(.*)', web.StaticFileHandler, {'path': config.app_dir('static')})
    ])
    # https://github.com/tornadoweb/tornado/issues/2308
    asyncio.set_event_loop(asyncio.new_event_loop())
    app.listen(config.web_port())
    ioloop.PeriodicCallback(SocketHandler.ws_dump, 50).start()
    ioloop.IOLoop.instance().start()