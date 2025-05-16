import socket
import threading

# List to keep track of connected clients
clients = []

# Broadcast message to all clients
def broadcast(message, client_socket):
    for client in clients:
        # Send the message to all clients except the sender
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

# Handle a client
def handle_client(client_socket):
    while True:
        try:
            # Receiving message from client
            message = client_socket.recv(1024)
            if message:
                print(f"Received message: {message.decode('utf-8')}")
                # Broadcast the message to all other clients
                broadcast(message, client_socket)
            else:
                # Remove client if message is empty (client disconnected)
                clients.remove(client_socket)
                client_socket.close()
                break
        except:
            continue

# Main function to set up the server
def start_server():
    host = '127.0.0.1'  # Localhost (can change to any valid IP address)
    port = 5557  # Port to bind the server to

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server started on {host}:{port}")

    while True:
        client_socket, client_address = server.accept()
        print(f"New connection from {client_address}")

        # Add the client to the list of clients
        clients.append(client_socket)

        # Start a new thread to handle the client
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    start_server()
