#udp client
#Vismaya A M
import socket

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input("Enter message: ")

    while message.lower().strip() != 'stop':
        client_socket.sendto(message.encode(), (host, port))
        data, addr = client_socket.recvfrom(1024)
        print('Received from server: ' + data.decode())

        message = input("Enter message: ")

    client_socket.close()

if __name__ == '__main__':
    client_program()
'''output
Enter message: hai this is a test message
Received from server: got it
'''
