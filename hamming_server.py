import socket


def decode_hamming(received):
    """Decodes 7-bit Hamming code and corrects errors."""
    r = [int(bit) for bit in received]
    
    # Calculate parity bits
    p1 = r[0]
    p2 = r[1]
    p4 = r[3]
    d = [r[2], r[4], r[5], r[6]] #p2p1d3p0d2d1d0
    
    # Calculate parity check
    s1 = p1 ^ d[0] ^ d[1] ^ d[3]
    s2 = p2 ^ d[0] ^ d[2] ^ d[3]
    s4 = p4 ^ d[1] ^ d[2] ^ d[3]
    
    # Error position
    error_pos = s1 * 1 + s2 * 2 + s4 * 4
    
    if error_pos != 0:
        print(f"Error detected at position {error_pos-1}.")
        # Correct the error
        r[error_pos - 1] ^= 1
        d = [r[2], r[4], r[5], r[6]]
        print(f"Decoded Data: {''.join(map(str, d))}")
        return ''.join(map(str, d)), error_pos
    print("No error detected")
    print(f"Decoded Data: {''.join(map(str, d))}")
    return ''.join(map(str, d)), None
    


def server_program():
    host = '127.0.0.1'
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server is listening...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    try:
        while True:
            data = conn.recv(7).decode()
            if not data:
                break
            print(f"Recieved Data: {data}")
            corrected_data,error_pos = decode_hamming(data)

    finally:
        conn.close()


if __name__ == '__main__':
    server_program()
