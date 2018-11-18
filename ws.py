from socket import *


HOST, PORT = '127.0.0.1', 9000

#https://docs.python.org/2/howto/sockets.html


'''

    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), 80))
    serversocket.listen(5)

'''

s = socket(AF_INET,SOCK_STREAM)

#s.connect(("",9000))  #s.connect(addr) makes a connection
s.bind((HOST,PORT)) #   only visible within the same machine
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
s.settimeout(10.0)  #optional timeout
                    #s.settimeout(None)     


while True:
    c,a = s.accept() # c = cloent socket , a = address
    request = c.recv(1024)
    print (request)



    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    c.sendall(http_response) #can use send()
    c.close()



'''

    s.send("GET /index.html HTTP/1.0\n\n")   #send request
    data = s.recv(10000)    # get request
    s.close()   #shuts down the connection

'''
#s.gethostname()
'''
fragments = []

while not done :
    chunk = s.recv(1024)
    if not chunk:
        break
    fragments.append(chunk)

message = " ".join(fragments)
'''
def first (self, port=9000)