import socket
from math import log2

def createBinaryList(m):
	d={}
	maxi=len(bin(m)[2:])
	for i in range(1,m+1):
		b="0"*(maxi-len(bin(i)[2:]))+bin(i)[2:]
		d[i]=b
	print(d)
	return d

def detectError(data,d):
	ans=""
	temp=data[::-1]
	for i in range(0,len(temp)):
		#find the parity bits
		a=log2(i+1)
		if a==int(a):
			#its a parity bit
			index=d[i+1].index("1")
			count=0
			for x in d:
				if d[x][index]=='1':
					count+=int(temp[x-1])
			print(f"Parity at {i+1} position is {count}")
			if count%2==0:
				ans+="0"
			else:
				ans+="1"
	return ans[::-1]






def main():
	IP='127.0.0.1'
	PORT=12345

	serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	serverSocket.bind((IP,PORT))
	serverSocket.listen(10)
	while True:
		clientSocket,address=serverSocket.accept()
		print(f"{address[0]} : {address[1]} Connected!")
		data=clientSocket.recv(1024).decode("utf-8")
		print(f"Data Received from Client : {data}")
		#to introduce error, at i position
		#data=data[:7]+"1"+data[8:]
		#print(f"Tampered Data : {data}")
		print("Error Detection Starts........")
		d=createBinaryList(len(data))

		position=detectError(data,d)
		position=int(position,2)

		if position==0:
			print("No Error!")
		else:
			print(f"Error at {position} Position from right")

		break
	serverSocket.close()
if __name__=='__main__':
	main()