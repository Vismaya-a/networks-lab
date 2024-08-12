import socket
import random

def encode_hamming(data):
    # Data bits
    d = [int(bit) for bit in data]
    
    # Parity bits
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p4 = d[1] ^ d[2] ^ d[3]
    
    # Hamming code
    hamming_code = [p1, p2, d[0], p4, d[1], d[2], d[3]]
    return ''.join(map(str, hamming_code))

def introduce_error(encoded_data):
    error_position = random.randint(0, 6)  # Error can be at any position from 0 to 6
    corrupted_data = list(encoded_data)
    print(f"Inserted error at position {error_position}")
    corrupted_data[error_position] = '0' if encoded_data[error_position] == '1' else '1'
    
    return ''.join(corrupted_data)

def client_program():
    host = '127.0.0.1'
    port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        while True:
            data = input("Enter 4-bit data (e.g., 1010): ")
            if len(data) != 4 or not all(bit in '01' for bit in data):
                print("Invalid input. Please enter exactly 4 bits.")
                continue

		
            encoded_data = encode_hamming(data)
            print(f"Original encoded data: {encoded_data}")
            corrupt = int(input("Corrupt the data: 1 for YES, 0 for NO: "))
            if corrupt:
            	encoded_data = introduce_error(encoded_data)
            	print(f"Corrupted data: {encoded_data}")
         
            client_socket.sendall(encoded_data.encode())

    finally:
        client_socket.close()

if __name__ == '__main__':
    client_program()

