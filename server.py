from socket import *

#https://docs.python.org/2/howto/sockets.html


'''

serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 80))
serversocket.listen(5)

'''

s = socket(AF_INET,SOCK_STREAM)

s.connect(("www.python.org",80))  #s.connect(addr) makes a connection
s.bind(("127.0.0.1",9000)) #   only visible within the same machine
s.listen(5)


# while 1:

while True:
    c,a = s.accept()
    print ("Received connection from", a)
    c.send("Hello %s\n" % a[0])
    c.close()





s.send("GET /index.html HTTP/1.0\n\n")   #send request
data = s.recv(10000)    # get request
s.close()   #shuts down the connection

