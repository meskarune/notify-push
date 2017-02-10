#!/usr/bin/env python

import asyncio
import ssl

class EchoServerClientProtocol(asyncio.Protocol):
    """Send Data in uppercase to all clients"""
    clients = {}

    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(self.peername))
        self.transport = transport
        self.clients[self.peername] = self.transport

    def connection_lost(self, exception):
        print('Client {0} disconnected: {1}'.format(self.peername, exception))
        del self.clients[self.peername]

    def data_received(self, data):
        message = data.decode("utf-8", "replace").strip()
        if message.lower() == "quit":
            print('Closing client {0} socket'.format(self.peername))
            self.transport.write("Quiting...".encode())
            self.transport.close()
        else:
            print('Data received: {!r}'.format(message))
            print('Send: {!r}'.format(message.upper()))
            for client, connection in self.clients.items():
                connection.write("{0}\n".format(message.upper()).encode())

if __name__ == '__main__':
    sc = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    sc.load_cert_chain('selfsigned.cert', 'selfsigned.key')

    loop = asyncio.get_event_loop()
    coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888, ssl=sc)
    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
