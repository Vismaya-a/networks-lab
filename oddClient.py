#single Chat Client
#Vismaya A M
import socket
def client_program():
    host = socket.gethostname() 
    port = 5000 

    client_socket = socket.socket()  
    client_socket.connect((host, port)) 

    message = input("Enter the number : ")  

    while message.lower().strip() != 'stop':
        client_socket.send(message.encode())  
        data = client_socket.recv(1024).decode()  
        print('Received from server: ' + data)  

        message = input("Enter the number : ")  

    client_socket.close()  


if __name__ == '__main__':
    client_program()
'''output
Enter the number : 3
Received from server: odd
Enter the number : 4
Received from server: even'''
