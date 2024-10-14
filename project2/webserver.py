'''

    webserver.py 2.0

    Author: Curtis Kauer
    
'''

import socket
import argparse
import os.path
import mimetypes

# parse commandline
argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("--port_number", "-p", type = int, required = True, help = "the port to listen on")

'''

    create_response - Creates responses
    arg1 - response_extension - the extension for the file requested
    return - response - returns the created response
    If the file is not found, sends 404 error response

'''
def create_response(response_extension):
    
    mime_type, encoding = mimetypes.guess_type(response_extension)
    
    response_header = ''
    content_length = 0
    body = ''
    
    # error catching if mime_type returned from guess_type is NoneType
    if type(mime_type) == type(None):
        mime_type = 'text/plain'
    
    content = "Content-Type: " + mime_type + "\r\n"
        
    try:
        with open(response_extension, "rb") as fp:
            data = fp.read()   # Read entire file
            body += data.decode()
    except FileNotFoundError:
        # File not found or other error
        body = "404 not found"
        response_header = "HTTP/1.1 404 Not Found\r\n"
    
    if len(response_header) == 0:
        response_header = "HTTP/1.1 200 OK\r\n"
        
    content_length = "Content-Length: " + str(len(body)) + "\r\n"
    connection = "Connection: close\r\n\r\n"        
   
    response = response_header + content + content_length + connection + body   
    
    return response

def main():
    
    port = argument_parser.parse_args()
    
    # sets up socket to listen for connections
    current_socket = socket.socket()
    network = ('', port.port_number)
    current_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    current_socket.bind(network)
    current_socket.listen()
    
    # infinite loop to listen for connections
    while True:
        
        decoded_data = ''
        new_connection = current_socket.accept()
        new_socket = new_connection[0]
        
        while (encoded_data := new_socket.recv(40)):
            decoded_data += encoded_data.decode()
            if decoded_data.find('\r\n\r\n') != -1:
            #    new_socket.close()
                break        
        print(decoded_data, end="")
        
        # Parses decoded header data
        header_lines = decoded_data.split('\r\n')
        
        # Parses first line of header
        header_first_line = header_lines[0]
        header_first_line = header_first_line.split(' ')
        path = header_first_line[1]
        
        # Parses file path
        file_name = os.path.split(path)[-1]
        
        # Create responses
        if len(file_name) == 0:
            file_name = 'index.html'
        
        response = create_response(file_name)
        response = response.encode()
        
        # Send responses
        new_socket.sendall(response)        
        new_socket.close()

if __name__ == "__main__":
    main()
