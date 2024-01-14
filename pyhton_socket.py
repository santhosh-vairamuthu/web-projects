# Import the socket module
import socket

# Create a socket object using IPv4 and TCP
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server 'example.com' on port 80
mysock.connect(('example.com', 80))

# Create an HTTP GET request for the root path '/'
cmd = 'GET https://example.com HTTP/1.0\r\n\r\n'.encode()
# Send the HTTP GET request to the server
mysock.send(cmd)

# Receive and print the data in chunks of 512 bytes until there is no more data
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

# Close the socket connection
mysock.close()
