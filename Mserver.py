#Multichat server
#Vismaya A M
import socket
import threading

# Function to handle each client's connection
def handle_client(client_socket, addr, clients):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                print(f"[{addr}] disconnected")
                clients.remove(client_socket)
                client_socket.close()
                break
            print(f"[{addr}] {message}")

            # Broadcast the message to all other clients
            message = '[' + str(addr) + '] ' + message
            for client in clients:
                if client != client_socket:
                    try:
                    	client.send(message.encode())
                    except:
                        clients.remove(client)
                        client.close()
        except Exception as e:
            print(e)
            break

def broadcast(message, clients):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            clients.remove(client)
            client.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5557))
    server_socket.listen(5)

    print("[SERVER] Server is listening on port 5557...")

    clients = []

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)

        # Create a new thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, addr, clients))
        client_thread.start()

        # Send a welcome message to the new client
        welcome_message = "Welcome to the chat server!"
        client_socket.send(welcome_message.encode())

        # Thread to handle server messages
        server_message_thread = threading.Thread(target=handle_server_messages, args=(clients,))
        server_message_thread.start()

def handle_server_messages(clients):
    while True:
        server_message = input("")
        server_message = '[Server] ' + server_message
        broadcast(server_message, clients)

if __name__ == '__main__':
    start_server()
''' output
[SERVER] Server is listening on port 5557...
[NEW CONNECTION] ('127.0.0.1', 46540) connected.
[NEW CONNECTION] ('127.0.0.1', 46542) connected.
[('127.0.0.1', 46540)] client1
[('127.0.0.1', 46542)] client2
'''



