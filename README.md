# notify-push
Push notifications out from a server to multiple clients using libnotify

## Requirements

Python3
Python asyncio
libnotify installed on client computers

## Server

Run the server with "python3 notify-push-server.py"

Currently its hardcoded to localhost:8888

## Client

Run the client with "python notify-push-client.py"

Currently hardcoded to connect to localhost:8888

# Todo

* Add configuration file to set host and port on the client and server
* Connect over SSL
* Add client authentification system
* Capture notify-send events from host? (idk if I need this)
