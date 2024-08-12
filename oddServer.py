#single Chat Server
#Vismaya A M
import socket

def server_program():
   
    host = socket.gethostname()
    port = 5000  

    server_socket = socket.socket()  
   
    server_socket.bind((host, port)) 

    
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        print("from client user: " + str(data))
        if(int(data)%2==0):
        	result="even"
        else:
        	result="odd"
        conn.send(result.encode())  

    conn.close()  


if __name__ == '__main__':
    server_program()
'''output
Connection from: ('192.168.10.108', 53066)
from client user: 3
from client user: 4
'''
