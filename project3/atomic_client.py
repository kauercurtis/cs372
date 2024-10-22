'''

atomic_client.py - a web client for getting NIST's (National Institute of Standards and Technology)

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
    
    # sets up a remote
    address = 'time.nist.gov'
    port = 37
    remote = (address, port)
    
    # connects
    current_socket = socket.socket()
    current_socket.connect(remote)
    
    # gets the 4 time from server and closes
    bytes = current_socket.recv(4) 
    current_socket.close()
    
    nist_time = int.from_bytes(bytes, 'big')
    print('NIST time  : ', nist_time)
    print('System time: ', system_seconds_since_1900())
    
if __name__ == "__main__":
    main()
