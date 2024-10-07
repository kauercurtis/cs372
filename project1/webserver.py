import socket
import argparse

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("--port_number", "-p", type = int, required = True, help = "the port to listen on")

def main():
    
    port = argument_parser.parse_args()
    
    current_socket = socket.socket()
    network = ('', port.port_number)
    current_socket.bind(network)
    current_socket.listen()
    
    while True:
        
        new_connection = current_socket.accept()
        new_socket = new_connection[0]
    
        while b'\r\n\r\n' not in (encoded_data := new_socket.recv(40)):
            data = encoded_data.decode()
            print(data, end="")
        
        data = encoded_data.decode()
        print(data, end="")
        
        ok_response = "HTTP/1.1 200 OK\r\n"
        content = "Content-Type: text/plain\r\n"
        content_length = "Content-Length: 6\r\n"
        connection = "Connection: close\r\n\r\n"
        greeting = "Hello!"
        response = ok_response + content + content_length + connection + greeting
        response = response.encode()
        
        new_socket.sendall(response)
        
        new_socket.close()

if __name__ == "__main__":
    main()
