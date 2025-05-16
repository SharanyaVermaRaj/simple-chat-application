import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(message.decode('utf-8'))
            else:
                print("Connection closed by the server.")
                break
        except:
            print("Error receiving message.")
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input()  # Take user input
        client_socket.send(message.encode('utf-8'))  # Send message to the server

# Main function to set up the client
def start_client():
    host = '127.0.0.1'  # Server's IP address
    port = 5557  # Port number (must be the same as the server's)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Start a thread to receive messages
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    # Start sending messages to the server
    send_messages(client_socket)

if __name__ == "__main__":
    start_client()
