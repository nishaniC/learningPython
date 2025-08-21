# here are our goals:
#
# we want to write a program which reads the address of a WWW site (e.g., pythoninstitute.org) using the standard input() function and fetches the root document
# (the main HTML document of the WWW site) of the specified site;
# the program outputs the document to the screen;
# the program uses TCP to connect to the HTTP server.

# create a new socket able to handle connection-oriented transmissions based on TCP;
# connect the socket to the HTTP server of a given address;
# send a request to the server (the server wants to know what we want from it)
# receive the server's response (it will contain the requested root document of the site)
# close the socket (end the connection)

# The socket module contains all the tools we need to deal with sockets.
import socket
server_addr = input("What server do you want to connect to? ")
# it can be the domain name of the server (like www.pythoninstitute.org, but without the leading http://)
# it can be the IP address of the server (like 87.98.235.184), but it must be said firmly that this variant is potentially ambiguous.
# Why? Because there can be more than one HTTP server located at the same IP address - the server you will reach may be not the server you intended to connect to.

#first argument specify the Internet socket domain; as different domains require completely different socket countenance, the target domain has to be known at the moment;
# the second argument is a socket type code (we may use the SOCK_STREAM symbol here to specify a high-level socket able to act as a character device -
# a device that can handle single characters,# as we are interested in transferring data byte by byte, not as fixed sized blocks
# (e.g., a terminal is a character device, while a disk isn't)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# the sock socket  is prepared to work on top of TCP protocol - it has the default socket configuration.

# You may ask - why 80? Can I put something else instead of this? No, you can’t. 80 is a well-known service number for HTTP.
# Any Internet browser will try to connect to port number 80 by default, so we do it, too.
# If something goes wrong, the connect() method (and any other method whose results may be unsuccessful) raises an exception(socket.gaierror( this means get address info error),
# ConnectionRefusedError ,socket.timeout).
sock.connect((server_addr, 80))

# A conversation with the HTTP server consists of requests (sent by the client) and responses (sent by the server).
# HTTP defines a set of acceptable requests - these are the request methods or HTTP words. The method asking the server to send a particular document of a given name is called GET
# To get a root document from a site named www.site.com the client should send the request containing a correctly formed GET method description:
# GET / HTTP/1.1\r\n
# Host: www.site.com\r\n
# Connection: close\r\n
# \r\n
# The GET method requires:
# a line containing the method name (i.e., GET) followed by the name of the resource the client wants to receive; the root document is specified as a single slash (i.e., /); the line must also include the HTTP protocol version (i.e., HTTP/1.1) and must end with the characters \r\n; note: all lines must end the same way;
# a line containing the name of the site (e.g., www.site.com) preceded by the parameter name (i.e., Host:)
# a line containing a parameter named Connection: along with its value close, which forces the server to close the connection after the first request is served; it will simplify our client's code;
# an empty line is a request terminator.

# The send() method doesn't natively accept strings - this is why we have to use the b prefix before the literal parts of the request string
# (it silently translates the string into bytes - an immutable vector consisting of values from the range 0..255, which send() likes most) and this is also why we should
# invoke bytes() to translate the string variable in the same manner.
#
# Note: the bytes' second argument specifies the encoding used to store the server's name. UTF8 seems to be the best choice for most modern OSs.
#
# The action performed by the send() method is extremely complicated - it engages not only many layers of the OS, but also lots of network equipment deployed
# on the route between the client and server, and obviously the server itself.
# The send() method doesn't natively accept strings - this is why we have to use the b prefix before the literal parts of the request string (it silently translates the string into bytes - an immutable vector consisting of values from the range 0..255, which send() likes most) and this is also why we should invoke bytes() to translate the string variable in the same manner.
#
# Note: the bytes' second argument specifies the encoding used to store the server's name. UTF8 seems to be the best choice for most modern OSs.
#
# The action performed by the send() method is extremely complicated - it engages not only many layers of the OS, but also lots of network equipment deployed on the route between the client and server, and obviously the server itself.
sock.send(b"GET / HTTP/1.1\r\nHost: " +
          bytes(server_addr, "utf8") +
          b"\r\nConnection: close\r\n\r\n")

# The recv() method waits for the server's response, gets it, and puts it inside a newly created object of type bytes
# The argument specifies the maximal acceptable length of the data to be received. If the server's response is longer than this limit, it will remain unreceived.
# You will need to invoke recv() again (maybe more than once) to get the remaining part of the data. It's a general practice to invoke recv() as long as it returns some data.
reply = sock.recv(10000)

# Invoking shutdown() is like a message whispered directly into the server's ear: "We have no more to say to you. We don't want to hear from you, either. The rest is silence."
# The following function arguments say more about our views for the future:
# socket.SHUT_RD - we aren't going to read the server's messages anymore (we declare ourselves deaf)
# socket.SHUT_WR - we won't say a word (actually, we'll be dumb)
# socket.SHUT_RDWR - specifies the conjunction of the two previous options.
sock.shutdown(socket.SHUT_RDWR)

sock.close()

# we'll just print it out using the built-in repr() function, which takes care of the clear (almost) textual presentation of any object
print(repr(reply))