import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    while True:
        message = input("Enter a message to encrypt (or type '0' to quit): ")
        if message == '0':
            print("Closing connection...")
            client.close()
            break

        # Get the number of rails from the user
        rails = input("Enter the number of rails to use for encryption: ")
        
        # Send both message and rails to the server, separated by '|'
        client.send(f"{message}|{rails}".encode())

        # Receive the encrypted message from the server
        encrypted_message = client.recv(1024).decode()
        print(f"Encrypted message from server: {encrypted_message}")

if __name__ == "__main__":
    main()
