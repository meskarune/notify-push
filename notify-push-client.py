#!/usr/bin/env python3

import asyncio
import ssl
import subprocess

class NotifySend():
    def notify(self, **kwargs):
        subprocess.call(["notify-send",
                         kwargs.get('title'),
                         kwargs.get('message'),
                         kwargs.get('icon')])
    #notify-send "This is the Title" "This is the message" -i /usr/share/icons/Adwaita/48x48/categories/preferences-system.png

class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, loop):
        self.loop = loop

    def connection_made(self, transport):
        print('Connected to server 127.0.0.1 on port 8888')
        transport.write("hello this is a test message.".encode())

    def data_received(self, data):
        print(data.decode("utf-8", "replace").strip())
        subprocess.call(["notify-send", data.decode("utf-8", "replace").strip()])

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()

if __name__ == '__main__':
    sc = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile='selfsigned.cert')
    loop = asyncio.get_event_loop()
    coro = loop.create_connection(lambda: EchoClientProtocol(loop), '127.0.0.1', 8888, ssl=sc)
    loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    loop.close()
