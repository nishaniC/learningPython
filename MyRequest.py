# The requests module in Python is a popular and powerful HTTP library that makes it easy to send web requests and interact with APIs or websites.
# It’s often described as “HTTP for Humans” because it simplifies complex networking tasks
import requests

#  initiates execution of the HTTP GET method and receives the server's response(it will try to connect the server, form a GET request, and accept the answer.)
# The only details we need to provide are the server’s address and the service port number – just like we did while using the browser’s address line.
# Note: the port number can be omitted if it is equal to 80, HTTP’s default port.
# the get() function returns a result. It’s an object containing all the information describing the GET method’s execution.

try:
    # timeout – it's the maximum time (measured in seconds and expressed as a real number)
    reply = requests.get('http://localhost:3000',timeout=1)
except requests.exceptions.Timeout:
    print('Sorry, Mr. Impatient, you didn\'t get your data')
else:
    print('Here is your data, my Master!')
print(reply.status_code)

# The requests module offers many different ways of specifying and recognizing status codes
print(requests.codes.__dict__)

if reply.status_code == requests.codes.ok:
    print("Success")

# The server's response consists of two parts: the header and the contents. Both parts have their representation in the object returned by the get() function
print("reply.headers: ",reply.headers)

# Most of the headers content aren't of any interest to us, although some are crucial, e.g., Content-Type, which describes what the server response's contents really are.
#
# You can access it directly using a routine dictionary lookup, just like this:
print("reply.headers['Content-Type']: ",reply.headers['Content-Type'])

# The raw response's contents are stored by the text property:
print("reply.text: ",reply.text)
# HTTP method GET is used to transfer a resource from server to the client
# HTTP method PUT is used to transfer a resource from client to the server, the resource being sent is intended to replace the previously stored data
# HTTP method DELETE is used to order the server to remove a resource from a given identification; the resource is unavailable from then on
# the other HTTP methods are HEAD,CONNECT,OPTIONS,TRACE
# all the listed HTTP methods have their reflections (or rather siblings) within the requests module
# All requests functions are in the habit of raising an exception when they encounter any kind of communication problem


try:
    # it’s addressing its efforts to port 3001, while our server is listening at port 3000
    reply = requests.get('http://localhost:3001', timeout=1)
except requests.exceptions.ConnectionError:
    print('Nobody\'s home, sorry!')
else:
    print('Everything fine!')

try:
    reply = requests.get('http:////////////')
except requests.exceptions.InvalidURL:
    print('Recipient unknown!')
else:
    print('Everything fine!')

# RequestException
# |___HTTPError
# |___ConnectionError
# |   |___ProxyError
# |   |___SSLError
# |___Timeout
# |   |___ConnectTimeout
# |   |___ReadTimeout
# |___URLRequired
# |___TooManyRedirects
# |___MissingSchema
# |___InvalidSchema
# |___InvalidURL
# |   |___InvalidProxyURL
# |___InvalidHeader
# |___ChunkedEncodingError
# |___ContentDecodingError
# |___StreamConsumedError
# |___RetryError
# |___UnrewindableBodyError