#!/usr/bin/env python3

import asyncio
import subprocess

class NotifySend():
    def notify(self, **kwargs):
        subprocess.call(["notify-send",
                         kwargs.get('title'),
                         kwargs.get('message'),
                         kwargs.get('icon')])
    #notify-send "This is the Title" "This is the message" -i /usr/share/icons/Adwaita/48x48/categories/preferences-system.png

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.loop = loop

    def connection_made(self, transport):
        print('Connected to server 127.0.0.1 on port 8888')

    def data_received(self, data):
        print(data.decode("utf-8", "replace").strip())
        subprocess.call(["notify-send", data.decode("utf-8", "replace").strip()])

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    message = 'Hello World!'
    coro = loop.create_connection(lambda: EchoClientProtocol(message, loop),
                              '127.0.0.1', 8888)
    loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    loop.close()
