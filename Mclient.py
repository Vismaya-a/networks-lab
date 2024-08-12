#Multichat client
#Vismaya A M
import socket
import threading

# Function to receive messages
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            break

# Setup client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5557))

    # Start a thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    message = input()

    while True:
        client_socket.send(message.encode())
        message = input()

if __name__ == '__main__':
    start_client()

'''output
client1
Welcome to the chat server!
client1
[('127.0.0.1', 46542)] client2
client2
Welcome to the chat server!
[('127.0.0.1', 46540)] client1
client2'''

