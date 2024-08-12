#udp server
#Vismaya A M
import socket
def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))

    print("Waiting for incoming connection...")

    while True:
        data, addr = server_socket.recvfrom(1024)
        message = data.decode()
        print("from client user: " + message)

        if message.lower() == "stop":
            print("Server is stopping...")
            break

        data = input('Enter message: ')
        server_socket.sendto(data.encode(), addr)

    server_socket.close()

if __name__ == '__main__':
    server_program()
'''output
Waiting for incoming connection...
from client user: hai this is a test message
Enter message: got it
'''
