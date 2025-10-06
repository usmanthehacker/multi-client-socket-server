import socket
import threading

HOST = '127.0.0.1'
PORT = 9999

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print("\n" + message)
            else:
                break
        except:
            print("Connection closed.")
            break

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    # Thread for receiving messages
    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    print("Connected to chat server. Type your message:")
    while True:
        message = input("")
        if message.lower() == "exit":
            break
        client_socket.send(message.encode())

    client_socket.close()

if __name__ == "__main__":
    start_client()
