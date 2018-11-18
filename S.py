import socket
import threading


HOST, PORT = '0.0.0.0', 9000

#https://docs.python.org/2/howto/sockets.html


'''

    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), 80))
    serversocket.listen(5)

'''

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # socket library, socket method (pass socket method)



#s.connect(("",9000))  #s.connect(addr) makes a connection
s.bind((HOST,PORT)) #   only visible within the same machine
                    # Tuple (() )
#s.bind(('', 80)) specifies that the socket is reachable by any address the machine happens to have.

s.listen(5)

print ('Serving HTTP on port %s ...' % PORT)
# while 1: # I think python V-2


''' 
    # accept connections from outside
    (clientsocket, address) = serversocket.accept()
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    ct = client_thread(clientsocket)
    ct.run()
'''
#s.settimeout(10.0)  #optional timeout
                    #s.settimeout(None)     


connections =[]   #for connections empty list

def handler (con,add):
    global connections
    while True:
        request = con.recv(1024) #data recive 1024 byts

        for connect in connections:
            connect.send(bytes(request))

        if not request:  
            connections.remove(con) 
            con.close()
            break  #if no data, loop will break 



# con = connection socket , a = address



while True:
    con,add = s.accept()
    
    conThread = threading.Thread(target=handler , args=(con,add))   #threading library thread method
    conThread.daemon = True #wont end until all the threads are done
    conThread.start() #start connetcion

    connections.append(con)
    print(connections)



    
    request = con.recv(1024)
    print (request)



"""
    c.sendall(http_response) #can use send()
    c.close()



'''

    s.send("GET /index.html HTTP/1.0\n\n")   #send request
    data = s.recv(10000)    # get request
    s.close()   #shuts down the connection

'''
#s.gethostname()
fragments = []

while not done :
    chunk = s.recv(1024)
    if not chunk:
        break
    fragments.append(chunk)

message = " ".join(fragments)
"""