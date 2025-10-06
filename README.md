# multi-client-socket-server
A Simple  Python socket server that handles multiple clients using threading
# Multi-Client Socket Server

A simple Python socket server and client that handles multiple clients simultaneously using **threading**. Messages from one client are **broadcast** to all other connected clients.

---

## Features

- Handles multiple clients concurrently
- Thread-safe broadcast of messages
- Graceful handling of client disconnections
- Simple and easy-to-understand Python code

---

## Requirements

- Python 3.x
- Standard library only (`socket`, `threading`)

---

## Files

- `multiple_server_socket.py` → The server script
- `multiple_client_socket.py` → The client script

---

## How to Run

### 1. Run the server:

```bash
python multiple_server_socket.py
