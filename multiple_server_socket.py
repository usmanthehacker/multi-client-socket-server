import socket
import threading

# Server config
HOST = '0.0.0.0'
PORT = 9999

# Thread lock for safe access
client_lock = threading.Lock()

# List of all connected clients
clients = []

# Function to handle each client
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    with client_lock:
        clients.append(conn)  # Add client to list safely

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                print(f"[DISCONNECTED] {addr}")
                with client_lock:
                    if conn in clients:
                        clients.remove(conn)
                conn.close()
                break

            print(f"[{addr}] {data}")
            broadcast(f"{addr} says: {data}", conn)

        except ConnectionResetError:
            print(f"[ERROR] Connection lost from {addr}")
            with client_lock:
                if conn in clients:
                    clients.remove(conn)
            conn.close()
            break

# Function to send message to all clients except sender
def broadcast(message, sender_conn):
    with client_lock:#one time just one thread threading sincronization
        snapshot = clients[:]#copy the list safe method 
    for client in snapshot:
        if client is sender_conn:#ye check krta he keh sender ko dubara message na chala jae
            continue
        try:
            client.send(message.encode())
        except Exception:
            with client_lock:
                if client in clients:
                    clients.remove(client)
            client.close()

# Main server starter
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
