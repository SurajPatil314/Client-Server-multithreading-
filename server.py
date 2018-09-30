import socket 
from threading import Thread 

class threadclass(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        #thread system function to initiate thread
        self.ip = ip
        self.port = port 
        print("New thread started at:: " + ip + "::" + str(port)) 
 
    def run(self): 
        while True : 
            istring = c.recv(1000) 
            #istring is input string from client          
            if not istring:
                print("input string is empty")
                break
                #if input is empty then break connection
            ostring = istring[::-1] 
            #reverse string function
            c.send(ostring)
            #send reversed string as a response to client



IPaddress = '127.0.0.1'
PORTnumber = 3400
#host = localhost IP address
#PORTnumber= random port number to connect
sa = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sa.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
#created TCP/IP socket
sa.bind((IPaddress, PORTnumber)) 
#associated socket with address
threads = []  
#created Thread pool
while True: 
    sa.listen(5) 
    #maximum connection limit
    print("Server is listening..." )
    (c, (ip,port)) = sa.accept() 
    #opened connection between the server and client
    newthread = threadclass(ip,port) 
    #for each new client, created new thread
    newthread.start() 
    threads.append(newthread) 
    #added all threads in thread pool
 
for t in threads: 
        t.join() 
#thread pool for loop
  
    
    
    
    
 