import socket

def create_playfair_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is usually omitted in the Playfair cipher.
    matrix = []
    key = key.upper().replace("J", "I")
    
    # Remove duplicates and add key to matrix
    used_letters = set()
    for letter in key:
        if letter not in used_letters and letter in alphabet:
            matrix.append(letter)
            used_letters.add(letter)

    # Add remaining letters
    for letter in alphabet:
        if letter not in used_letters:
            matrix.append(letter)
            used_letters.add(letter)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(letter, matrix):
    for i, row in enumerate(matrix):
        if letter in row:
            return i, row.index(letter)
    return None

def playfair_cipher(message, key, encrypt=True):
    matrix = create_playfair_matrix(key)
    message = message.upper().replace("J", "I").replace(" ", "")
    if len(message) % 2 != 0:
        message += 'X'  # Add padding

    result = []
    for i in range(0, len(message), 2):
        a, b = message[i], message[i + 1]
        row_a, col_a = find_position(a, matrix)
        row_b, col_b = find_position(b, matrix)

        if row_a == row_b:
            if encrypt:
                result.append(matrix[row_a][(col_a + 1) % 5])
                result.append(matrix[row_b][(col_b + 1) % 5])
            else:
                result.append(matrix[row_a][(col_a - 1) % 5])
                result.append(matrix[row_b][(col_b - 1) % 5])
        elif col_a == col_b:
            if encrypt:
                result.append(matrix[(row_a + 1) % 5][col_a])
                result.append(matrix[(row_b + 1) % 5][col_b])
            else:
                result.append(matrix[(row_a - 1) % 5][col_a])
                result.append(matrix[(row_b - 1) % 5][col_b])
        else:
            result.append(matrix[row_a][col_b])
            result.append(matrix[row_b][col_a])

    return ''.join(result)

def handle_client(client_socket):
    key = "PLAYFAIRCIPHER"
    while True:
        message = client_socket.recv(1024).decode()
        if not message:
            break
        print(f"Received from client: {message}")
        encrypted_message = playfair_cipher(message, key)
        print(f"Encrypted message: {encrypted_message}")
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
