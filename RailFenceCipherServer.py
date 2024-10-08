import socket

def rail_fence_encrypt(text, key):
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    direction_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if row == 0 or row == key - 1:
            direction_down = not direction_down
        
        rail[row][col] = text[i]
        col += 1

        row += 1 if direction_down else -1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

def handle_client(client_socket):
    while True:
        # Receive message from client
        message_data = client_socket.recv(1024).decode()
        if not message_data:
            break
        
        # The message_data is formatted as: "<message>|<key>"
        message, key = message_data.split('|')
        key = int(key)
        
        print(f"Received from client: {message} with {key} rails")
        encrypted_message = rail_fence_encrypt(message, key)
        print(f"Encrypted message: {encrypted_message}")
        
        # Send the encrypted message back to the client
        client_socket.send(encrypted_message.encode())

    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5555))
    server.listen(1)
    print("Server is listening on port 5555...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection established with {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()
