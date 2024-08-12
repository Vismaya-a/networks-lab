import socket
from math import log2

def getRedundantBits(m):
    for i in range(0,m):
        if 2**i>=m+i+1:
            return i

def placeBits(arr,data):
    #reverseArray
    temp=data[::-1]
    j=0
    for i in range(0,len(arr)):
        #i+1 is correct position
        a=log2(i+1)
        if a==int(a):
            pass
        else:
            arr[i]=temp[j]
            j+=1
    arr=arr[::-1]
    return arr

def createBinaryList(m):
    d={}
    maxi=len(bin(m)[2:])
    for i in range(1,m+1):
        b="0"*(maxi-len(bin(i)[2:]))+bin(i)[2:]
        d[i]=b
    print(d)
    return d

def fixParity(d,arr):
    temp=arr[::-1]
    #7 -> 0 to 6
    for i in range(0,len(temp)):
        #index is 
        if temp[i]!='R':
            pass
        else:
            #i+1 is redundant
            index=d[i+1].index("1")
            count=0
            for x in d:
                if d[x][index]=='1' and x!=i+1:
                    count+=int(temp[x-1])
            if count%2==0:
                temp=temp[:i]+'0'+temp[i+1:]
            else:
                temp=temp[:i]+'1'+temp[i+1:]
    return temp[::-1]

def main():
    IP='127.0.0.1'
    PORT=12345

    clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    clientSocket.connect((IP,PORT))

    data=input("Please Enter the Data : ")
    

    redundantBits=getRedundantBits(len(data))
    print("No of Redundant Bits required are : ",redundantBits)
    arr=['R']*(len(data)+redundantBits)
    arr=placeBits(arr,data)
    arr="".join(arr)
    print(f"Data After Posting Data & Redundant Bits : {arr}")
    d=createBinaryList(len(arr))
    codeword=fixParity(d,arr)

    error_choice = input("Do you want to introduce an error? (yes/no): ")
    if error_choice.lower() == 'yes':
        error_position = int(input("Enter the position of the error (from right): "))
        codeword = list(codeword)
        codeword[-error_position] = '1' if codeword[-error_position] == '0' else '0'
        codeword = ''.join(codeword)

    clientSocket.send(bytes(codeword,"utf-8"))
    print("Data Sent to server\n")


    clientSocket.close()


if __name__=='__main__':
    main()
