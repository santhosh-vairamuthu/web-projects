from socket import *

def createServer():
    # Create a socket object using IPv4 and TCP
    serversocket = socket(AF_INET, SOCK_STREAM)

    try:
        # Bind the server socket to the localhost on port 9000
        serversocket.bind(('localhost', 9000))
        # Listen for incoming connections with a backlog of 5
        serversocket.listen(5)

        print("Server listening on http://localhost:9000")

        while True:
            # Accept a client connection
            (clientsocket, address) = serversocket.accept()

            # Receive and decode the data sent by the client
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")

            if len(pieces) > 0:
                # Print the first line of the client's request (assuming it's the request line)
                print("Request:", pieces[0])

            # Prepare the HTTP response
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"

            # Send the HTTP response to the client
            clientsocket.sendall(data.encode())
            # Shutdown the write end of the socket (sending is done)
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("Error: \n")
        print(exc)
    finally:
        try:
            # Close the server socket
            serversocket.close()
        except:
            pass

# Call the createServer function to start the server
createServer()
