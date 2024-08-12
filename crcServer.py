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


def decodeData(data, key): 

	l_key = len(key) 
	appended_data = data + '0'*(l_key-1) 
	remainder = mod2div(appended_data, key) 
	return int(remainder)
	
	
def server_program():
   
	host = socket.gethostname()
	port = 5000  

	server_socket = socket.socket()  
	server_socket.bind((host, port)) 

	server_socket.listen(2)
	conn, address = server_socket.accept()
	print("Connection from: " + str(address))
	received_data = conn.recv(1024).decode()
	data, key = received_data.split(',')
	rem=decodeData(data,key)
	print("Remainder : ", rem) 
	if(rem ==0):
		print("no error")
	else:
		print("error")
	received_data = conn.recv(1024).decode()
	data, key = received_data.split(',')
	rem=decodeData(data,key)
	print("Remainder : ", rem) 
	if(rem ==0):
		print("no error")
	else:
		print("error")
	conn.close()  


if __name__ == '__main__':
	server_program()

