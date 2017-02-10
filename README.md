# notify-push
Push notifications out from a server to multiple clients using libnotify

## Requirements

* Python3
* Python asyncio
* libnotify installed on client computers

## Server

Run the server with "python3 notify-push-server.py"

Currently its hardcoded to localhost:8888

## Client

Run the client with "python notify-push-client.py"

Currently hardcoded to connect to localhost:8888

## Testing

Use netcat to send messages to the serve and all connected clients:

    nc localhost 8888

Type "quit" to disconect or hit ctrl c

## Create key/certificate for SSL

Make sure to set FQDN to 127.0.0.1 or whatever host you are using.

    openssl req -nodes -newkey rsa:2048 -keyout selfsigned.key -x509 -out selfsigned.cert

# Todo

* Add configuration file to set host and port on the client and server
* Connect over SSL
* Add client authentification system
* Capture notify-send events from host? (idk if I need this)
