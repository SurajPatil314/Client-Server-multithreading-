import socket 

def main(): 
    host = '127.0.0.1'
    port = 3400
    #host = localhost IP address
    #port= random port number to connect
    sa = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    sa.connect((host,port))  
    #created client connection with host ip address and port
    while True: 
        message = input("enter your string::")
        sa.send(message.encode('ascii')) 
        #sent string as a input to server in encoded ASCII format
        rdata = sa.recv(1000) 
        #received response from server
        print('Reverse string received from server :',str(rdata.decode('ascii'))) 
        ans = input('\nDo you want to send another input to server press y/n :') 
        if ans == 'y': 
            continue
        else: 
            break
    sa.close() 
    #closed connection
  
if __name__ == '__main__': 
    main()