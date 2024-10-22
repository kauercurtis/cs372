'''

webclient.py - a basic web client

Author: Curtis Kauer

'''

import socket
import time

def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta

    return seconds_since_1900_epoch

def main():
    
    remote = (arguments.web_domain, arguments.port_number)
    
    # builds request header    
    get_request = "GET / HTTP/1.1\r\n"
    host = "Host: " + remote[0] + "\r\n"
    connection = "Connection: close\r\n\r\n"
    request_header = get_request + host + connection
    encoded_header = request_header.encode()
    
    current_socket = socket.socket()
    current_socket.connect(remote)
    current_socket.sendall(encoded_header)
    
    # decodes packets
    while (encoded_data := current_socket.recv(40)) != b'':
        data = encoded_data.decode()
        print(data, end = "")
    
    current_socket.close()
    
if __name__ == "__main__":
    main()
