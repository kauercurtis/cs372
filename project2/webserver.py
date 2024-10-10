'''

    webserver.py

    Author: Curtis Kauer

'''

import socket
import argparse

# parse commandline
argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("--port_number", "-p", type = int, required = True, help = "the port to listen on")

'''

    create_response - Creates responses
    return - response - returns the created response
    Only returns static hard coded 200 ok responses.

'''
def create_response():
    
        ok_response = "HTTP/1.1 200 OK\r\n"
        content = "Content-Type: text/plain\r\n"
        content_length = "Content-Length: 6\r\n"
        connection = "Connection: close\r\n\r\n"
        greeting = "Hello!"
        
        response = ok_response + content + content_length + connection + greeting    
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
                break        
        print(decoded_data, end="")
        
        # Check for fully decoded header
        end_of_header_index = decoded_data.find('\r\n\r\n')
        if end_of_header_index == -1:
            print("End of Header Not Found!!!")
            return
        
        # Parses decoded header data
        header_lines = decoded_data.split('\r\n')
        
        # Parses first line of header
        header_first_line = header_lines[0]
        header_first_line = header_first_line.split(' ')
        path = header_first_line[1]
        
        # Create responses
        response = create_response()
        response = response.encode()
        
        new_socket.sendall(response)
        
        new_socket.close()

if __name__ == "__main__":
    main()
