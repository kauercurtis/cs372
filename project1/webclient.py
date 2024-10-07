'''

webclient.py - a basic web client

Author: Curtis Kauer

'''

import socket
import argparse

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("--web_domain", "-w", type = str, required = True, help = "the domain name of the website to connect to")
argument_parser.add_argument("--port_number", "-p", type = int, default = 80, help = "a specified port number to connect to, default is 80")
arguments = argument_parser.parse_args()

def main():
    
    remote = (arguments.web_domain, arguments.port_number)
        
    get_request = "GET / HTTP/1.1\r\n"
    host = "Host: " + remote[0] + "\r\n"
    connection = "Connection: close\r\n\r\n"
    request_header = get_request + host + connection
    encoded_header = request_header.encode()
    
    current_socket = socket.socket()
    current_socket.connect(remote)
    current_socket.sendall(encoded_header)
    
    while (encoded_data := current_socket.recv(40)) != b'':
        data = encoded_data.decode()
        print(data, end = "")
    
    current_socket.close()
    
if __name__ == "__main__":
    main()
