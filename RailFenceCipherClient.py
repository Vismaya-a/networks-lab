import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    while True:
        message = input("Enter a message to encrypt (or type '0' to quit): ")
        if message == '0':
            print("Closing connection...")
            client.close()  # Close the connection before exiting
            break
        client.send(message.encode())  # Send the message to the server
        encrypted_message = client.recv(1024).decode()  # Receive the encrypted message from the server
        print(f"Encrypted message from server: {encrypted_message}")

if __name__ == "__main__":
    main()
