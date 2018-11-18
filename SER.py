import socket
import threading
import sys
 


class server:
    def __init__ (self): # which is always executed when the class is being initiated.
        HOST, PORT = '0.0.0.0', 9000
        #https://docs.python.org/2/howto/sockets.html
        '''

            serversocket = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
            serversocket.bind((socket.gethostname(), 80))
            serversocket.listen(5)

        '''
        self.folder = 'web'

    def start (self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # socket library, socket method (pass socket method)
        
        try:
            print ('Starting server on port %s ...' % PORT)
            
            #s.connect(("",9000))  #s.connect(addr) makes a connection
            s.bind((HOST,PORT)) #   only visible within the same machine
                            # Tuple (() )
            #s.bind(('', 80)) specifies that the socket is reachable by any address the machine happens to have.
            print ('Server Started on port %s ...' % PORT)

        except Exception as e:
            print ('Error ! Could not bind to port on %s ...' % PORT)
            self.shutdown()
            sys.exit(1)
        self.incoming() #cheak for incoming requests


        

        
    def shutdown(self):
        try:
            print ('Shutting down server')
            s.socket.shutdown(socket.SHUT_RDWR) #RD = Read , WR = Write

        except Exception as e:
            pass #pass this , means port is alredy closed

    
    def makeHedder ():

        header = ''
        if responceCode == 200:
            header = header + 'HTTP/1.1 200 OK\n'
        elif responceCode == 404:
            header = header + 'HTTP/1.1 404 NOT Found \n'

        header = header + 'Connection Closed \n'

        return header

    def incoming(self):
        self.socket.listen(5)
        while True:
            con,add = self.s.accept()
            
            conThread = threading.Thread(target=self.handler , args=(con,add))   #threading library thread method
            conThread.daemon = True #wont end until all the threads are done
            conThread.start() #start connetcion

            connections.append(con)
            print(connections) 
        
            '''
                def handler (self,con,add):
                    global connections
                    while True:
                        request = con.recv(1024).decode() #data recive 1024 byts

                        if not request:  
                            connections.remove(con) 
                            con.close()
                            break  #if no data, loop will break 

                        if reqMethod 

            '''            
            '''
                        for connect in connections:
                            connect.send(bytes(request))

                        if not request:  
                            connections.remove(con) 
                            con.close()
                            break  #if no data, loop will break 
            '''


                        

                #print ('Serving HTTP on port %s ...' % PORT)
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


            # connections =[]   #for connections empty list

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
        
            print (request)


            if request_method == "GET" or request_method == "HEAD":
                #  "GET /index.html" split on space
                file_requested = data.split(' ')[1]

                # If get has parameters ('?'), ignore them
                #"GET /index.html?id=11" split on space
                file_requested =  file_requested.split('?')[0]

                if file_requested == "/":
                    file_requested = "/index.html"

                filepath_to_serve = self.folder + file_requested
                print("Serving web page [{fp}]".format(fp=filepath_to_serve))

                # Load and Serve files content
                try:
                    f = open(filepath_to_serve, 'rb')
                    if request_method == "GET": # Read only for GET
                        response_data = f.read()
                    f.close()
                    response_header = self.makeHedder(200)

                except Exception as e:
                    print("File not found. Serving 404 page.")
                    response_header = self.makeHedder(404)

                    if request_method == "GET": # Temporary 404 Response Page
                        response_data = b"<html><body><center><h1>Error 404: File not found</h1></center><p>Head back to <a href="/">dry land</a>.</p></body></html>"

                response = response_header.encode()
                if request_method == "GET":
                    response += response_data

                client.send(response)
                client.close()
                break
            else:
                print("Unknown HTTP request method: {method}".format(method=request_method))
    # con = connection socket , a = address


'''
while True:
    con,add = s.accept()
    
    conThread = threading.Thread(target=handler , args=(con,add))   #threading library thread method
    conThread.daemon = True #wont end until all the threads are done
    conThread.start() #start connetcion

    connections.append(con)
    print(connections)



    
    request = con.recv(1024)
    print (request)

'''
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