
import socket

def xor(a, b): 
	result = [] 
	for i in range(1, len(b)): 
		if a[i] == b[i]: 
			result.append('0') 
		else: 
			result.append('1') 

	return ''.join(result) 


def mod2div(dividend, divisor): 

	pick = len(divisor) 
	tmp = dividend[0: pick] 

	while pick < len(dividend): 

		if tmp[0] == '1': 
			tmp = xor(divisor, tmp) + dividend[pick] 

		else:
			tmp = xor('0'*pick, tmp) + dividend[pick] 

		pick += 1
	if tmp[0] == '1': 
		tmp = xor(divisor, tmp) 
	else: 
		tmp = xor('0'*pick, tmp) 

	checkword = tmp 
	return checkword 


def encodeData(data, key): 

	l_key = len(key) 
	appended_data = data + '0'*(l_key-1) 
	remainder = mod2div(appended_data, key) 

	# Append remainder in the original data 
	codeword = data + remainder 
	print("Remainder : ", remainder) 
	print("Encoded Data (Data + Remainder) : ", 
		codeword) 
	return codeword





def client_program():
	host = socket.gethostname() 
	port = 5000 

	client_socket = socket.socket()  
	client_socket.connect((host, port)) 
	
	data = input("Enter message: ")
	key=input("enter the key") 
	print("without error")
	data = ''.join(format(ord(i), '08b') for i in data)
	encodedData=encodeData(data,key)
	client_socket.send(f"{encodedData},{key}".encode())  
	#client_socket.send(encodedData.encode(),key.encode())  
	print("with error")
	encodedData=encodeData(data,key.replace('0','1'))
	client_socket.send(f"{encodedData},{key}".encode()) 
	client_socket.close()  


if __name__ == '__main__':
	client_program()

