# P2P Chat (Python)

Simple terminal peer-to-peer chat over TCP sockets.

## Status

This project is still under development.

Planned improvements include more in-depth, multi-platform text and file sharing features.

## Project Structure

- `src/project p2p/p2p.py` - host/server script
- `src/project p2p/p2pclient.py` - client script
- `src/project p2p/save.txt` - saved IP addresses used by the client

## Requirements

- Python 3.x
- Two devices on a reachable network
- Port `5000` open between devices

## Run

Use two terminals.

1. Start the host:

```powershell
cd "src/project p2p"
python p2p.py
```

2. Start the client (on same or another machine):

```powershell
cd "src/project p2p"
python p2pclient.py
```

3. In the client, enter the host machine IPv4 address when prompted.

## Usage

- Type messages and press Enter to send.
- Type `\q` and press Enter to close the chat.
- In client startup, enter `s` to pick from saved IP addresses.

## Notes

- Current implementation supports one host and one client connection.
- `p2pclient.py` reads/writes `save.txt` using a relative path, so run it from `src/project p2p` (or adjust paths in code).
